async function translateNumbers() {
    const input = document.getElementById("numberInput").value;
    const numbers = input.split(',').map(num => parseInt(num.trim()));

    const response = await fetch('/translate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ numbers })
    });

    if (response.ok) {
        const translatedNumbers = await response.json();
        const formattedOutput = translatedNumbers.map(num => `<div>${num}</div>`).join('');
        document.getElementById("result").innerHTML = formattedOutput;
    } else {
        document.getElementById("result").innerText = 'Error: Unable to translate numbers.';
    }
}

document.getElementById("numberInput").addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        translateNumbers();
    }
});
