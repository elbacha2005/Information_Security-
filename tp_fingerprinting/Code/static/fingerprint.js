// Collect features from browser APIs
const browserLanguage = navigator.language;
const allLanguages = navigator.languages.join(", ");
const screenRes = screen.width + "x" + screen.height;
const colorDepth = screen.colorDepth;
const pixelRatio = window.devicePixelRatio;
const timeZone = Intl.DateTimeFormat().resolvedOptions().timeZone;
const cpuCores = navigator.hardwareConcurrency;
const deviceMemory = navigator.deviceMemory || "not available";
const windowSize = window.innerWidth + "x" + window.innerHeight;

// Display on the page
const outputEl = document.getElementById("feature-output");
outputEl.innerHTML =
    "<strong>Language:</strong> " + browserLanguage + "<br>" +
    "<strong>All languages:</strong> " + allLanguages + "<br>" +
    "<strong>Screen:</strong> " + screenRes + "<br>" +
    "<strong>Color depth:</strong> " + colorDepth + "<br>" +
    "<strong>Pixel ratio:</strong> " + pixelRatio + "<br>" +
    "<strong>Time zone:</strong> " + timeZone + "<br>" +
    "<strong>CPU cores:</strong> " + cpuCores + "<br>" +
    "<strong>Device memory:</strong> " + deviceMemory + "<br>" +
    "<strong>Window size:</strong> " + windowSize + "<br>" +
    "<strong>Navigator:</strong> " + navigator.userAgent + "<br>";


// Send to server
const activeFeatures = {
    browserLanguage, allLanguages, screenRes,
    colorDepth, pixelRatio, timeZone,
    cpuCores, deviceMemory, windowSize
};

fetch("/collect", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(activeFeatures)
});

async function generateFingerprint() {
    const raw = [
        browserLanguage, allLanguages, screenRes,
        colorDepth, pixelRatio, timeZone,
        cpuCores, deviceMemory, windowSize
    ].join("|");

    const data = new TextEncoder().encode(raw);
    const hashBuffer = await crypto.subtle.digest("SHA-256", data);

    const hashHex = Array.from(new Uint8Array(hashBuffer))
        .map(b => b.toString(16).padStart(2, "0"))
        .join("");

    document.getElementById("fingerprint-output").textContent = hashHex;

    fetch("/collect", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ fingerprint: hashHex })
    });
}

setTimeout(generateFingerprint, 500);