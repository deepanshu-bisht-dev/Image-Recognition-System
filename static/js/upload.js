const scanner = document.getElementById("scanner");
const scannerContent = document.getElementById("scanner-content");
const fileInput = document.getElementById("file-input");
const previewImage = document.getElementById("preview-image");
const scanBtn = document.getElementById("scan-btn");
const statusText = document.getElementById("status-text");
const resultsGrid = document.getElementById("results-grid");

let selectedFile = null;

// ---- Click to browse ----
scanner.addEventListener("click", () => {
    if (!selectedFile) fileInput.click();
});

fileInput.addEventListener("change", (e) => {
    if (e.target.files.length) handleFile(e.target.files[0]);
});

// ---- Drag & drop ----
["dragenter", "dragover"].forEach(evt => {
    scanner.addEventListener(evt, (e) => {
        e.preventDefault();
        scanner.classList.add("drag-over");
    });
});

["dragleave", "drop"].forEach(evt => {
    scanner.addEventListener(evt, (e) => {
        e.preventDefault();
        scanner.classList.remove("drag-over");
    });
});

scanner.addEventListener("drop", (e) => {
    if (e.dataTransfer.files.length) handleFile(e.dataTransfer.files[0]);
});

function handleFile(file) {
    const validTypes = ["image/png", "image/jpeg", "image/webp"];
    if (!validTypes.includes(file.type)) {
        setStatus("UNSUPPORTED FORMAT — USE PNG / JPG / WEBP");
        return;
    }

    selectedFile = file;

    const reader = new FileReader();
    reader.onload = (e) => {
        previewImage.src = e.target.result;
        previewImage.style.display = "block";
        scannerContent.style.display = "none";
        setStatus("IMAGE LOADED — READY TO ANALYZE");
        scanBtn.disabled = false;
    };
    reader.readAsDataURL(file);

    resultsGrid.innerHTML = "";
}

function setStatus(text) {
    statusText.textContent = text;
}

// ---- Analyze button ----
scanBtn.addEventListener("click", async () => {
    if (!selectedFile) return;

    scanner.classList.add("analyzing");
    scanBtn.disabled = true;
    setStatus("ANALYZING...");
    resultsGrid.innerHTML = "";

    const formData = new FormData();
    formData.append("image", selectedFile);

    try {
        const res = await fetch("/api/predict", {
            method: "POST",
            body: formData,
        });
        const data = await res.json();

        // Keep the scan animation visible briefly for effect, then reveal results
        setTimeout(() => {
            scanner.classList.remove("analyzing");
            scanBtn.disabled = false;

            if (!res.ok) {
                setStatus(`ERROR — ${data.error || "ANALYSIS FAILED"}`);
                return;
            }

            setStatus("ANALYSIS COMPLETE");
            renderResults(data.predictions);
        }, 900);

    } catch (err) {
        scanner.classList.remove("analyzing");
        scanBtn.disabled = false;
        setStatus("ERROR — NETWORK ISSUE, TRY AGAIN");
    }
});

function renderResults(predictions) {
    resultsGrid.innerHTML = "";

    predictions.forEach((pred, i) => {
        const row = document.createElement("div");
        row.className = "result-row";
        row.style.animationDelay = `${i * 0.12}s`;

        const barClass = pred.confidence < 40 ? "mid" : "";

        row.innerHTML = `
            <span class="result-rank">0${i + 1}</span>
            <span class="result-label">${pred.label}</span>
            <div class="result-bar-track">
                <div class="result-bar-fill ${barClass}" data-width="${pred.confidence}"></div>
            </div>
            <span class="result-confidence">${pred.confidence}%</span>
        `;

        resultsGrid.appendChild(row);

        // Animate bar fill after insertion
        requestAnimationFrame(() => {
            const fill = row.querySelector(".result-bar-fill");
            setTimeout(() => {
                fill.style.width = `${pred.confidence}%`;
            }, 50);
        });
    });
}

// ---- Dark / Light theme toggle ----
const themeToggleBtn = document.getElementById("theme-toggle");
const themeIcon = document.getElementById("theme-icon");
const themeLabel = document.getElementById("theme-label");

function applyTheme(theme) {
    if (theme === "light") {
        document.documentElement.setAttribute("data-theme", "light");
        themeIcon.textContent = "☀";
        themeLabel.textContent = "LIGHT";
    } else {
        document.documentElement.removeAttribute("data-theme");
        themeIcon.textContent = "🌙";
        themeLabel.textContent = "DARK";
    }
}

// Load saved preference (defaults to dark)
const savedTheme = localStorage.getItem("vision-theme") || "dark";
applyTheme(savedTheme);

themeToggleBtn.addEventListener("click", () => {
    const current = document.documentElement.getAttribute("data-theme") === "light" ? "light" : "dark";
    const next = current === "light" ? "dark" : "light";
    applyTheme(next);
    localStorage.setItem("vision-theme", next);
});
