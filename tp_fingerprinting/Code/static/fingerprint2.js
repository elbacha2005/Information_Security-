const targetSentence = document.getElementById("target-sentence").textContent.trim();
const typingInput = document.getElementById("typing-input");
const restartBtn = document.getElementById("restart-btn");
const resultsDiv = document.getElementById("typing-results");

let startTime = null;
let backspaceCount = 0;
let finished = false;

// Start timer on first key + count backspaces
typingInput.addEventListener("keydown", function (event) {
    if (startTime === null && !finished) {
        startTime = performance.now();
    }
    if (event.key === "Backspace") {
        backspaceCount++;
    }
});

// Check if sentence matches after each character change
typingInput.addEventListener("input", function () {
    if (finished) return;

    if (typingInput.value === targetSentence) {
        finished = true;

        const totalTimeSec = (performance.now() - startTime) / 1000;
        const typingSpeed = (targetSentence.length / totalTimeSec).toFixed(2);

        resultsDiv.innerHTML =
            "<strong>Time:</strong> " + totalTimeSec.toFixed(2) + " s<br>" +
            "<strong>Speed:</strong> " + typingSpeed + " chars/s<br>" +
            "<strong>Corrections:</strong> " + backspaceCount;

        fetch("/collect", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                totalTime: totalTimeSec.toFixed(2),
                typingSpeed: typingSpeed,
                corrections: backspaceCount
            })
        });
    }
});

// Reset everything
restartBtn.addEventListener("click", function () {
    typingInput.value = "";
    startTime = null;
    backspaceCount = 0;
    finished = false;
    resultsDiv.innerHTML = "";
});