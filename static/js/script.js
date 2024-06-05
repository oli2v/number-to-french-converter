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
        document.getElementById("result").innerText = translatedNumbers.join(', ');
    } else {
        document.getElementById("result").innerText = 'Error: Unable to translate numbers.';
    }
}
