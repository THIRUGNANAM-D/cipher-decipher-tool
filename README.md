<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Majestic Flames Cipher Tool</title>
<style>
    body {
        margin: 0;
        font-family: Arial, sans-serif;
        background: url('https://i.ibb.co/k5wqkVx/flames-bg.jpg') no-repeat center center fixed;
        background-size: cover;
        position: relative;
        color: white;
    }
    body::after {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: rgba(0, 100, 255, 0.25); /* Blue mist overlay */
        z-index: -1;
    }
    .container {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        padding: 20px;
        gap: 10px;
        background: rgba(0, 0, 0, 0.5);
    }
    input, select, button {
        padding: 10px;
        border: none;
        border-radius: 5px;
    }
    input {
        width: 200px;
    }
    button {
        background: #ff4500;
        color: white;
        cursor: pointer;
    }
    button:hover {
        background: #ff6347;
    }
    .result {
        text-align: center;
        margin-top: 20px;
        font-size: 1.2em;
        background: rgba(0, 0, 0, 0.6);
        display: inline-block;
        padding: 10px 20px;
        border-radius: 5px;
    }
</style>
</head>
<body>
<div class="container">
    <input type="text" id="text" placeholder="Enter text">
    <select id="cipher">
        <option value="caesar">Caesar</option>
        <option value="vigenere">Vigenère</option>
        <option value="hill">Hill</option>
    </select>
    <input type="text" id="key" placeholder="Enter key">
    <button onclick="encrypt()">Encrypt</button>
    <button onclick="decrypt()">Decrypt</button>
</div>
<div class="result" id="output">Output will appear here</div>

<script>
function caesarShift(str, amount) {
    if (amount < 0) return caesarShift(str, amount + 26);
    return str.split('').map(char => {
        if (char.match(/[a-z]/i)) {
            let code = char.charCodeAt(0);
            if (code >= 65 && code <= 90)
                return String.fromCharCode(((code - 65 + amount) % 26) + 65);
            else if (code >= 97 && code <= 122)
                return String.fromCharCode(((code - 97 + amount) % 26) + 97);
        }
        return char;
    }).join('');
}

function vigenereEncrypt(text, key) {
    key = key.toUpperCase();
    let result = '';
    let j = 0;
    for (let i = 0; i < text.length; i++) {
        let c = text[i];
        if (/[a-z]/i.test(c)) {
            let offset = (key[j % key.length].charCodeAt(0) - 65);
            if (c === c.toUpperCase()) {
                result += String.fromCharCode((c.charCodeAt(0) - 65 + offset) % 26 + 65);
            } else {
                result += String.fromCharCode((c.charCodeAt(0) - 97 + offset) % 26 + 97);
            }
            j++;
        } else {
            result += c;
        }
    }
    return result;
}

function vigenereDecrypt(text, key) {
    key = key.toUpperCase();
    let result = '';
    let j = 0;
    for (let i = 0; i < text.length; i++) {
        let c = text[i];
        if (/[a-z]/i.test(c)) {
            let offset = (key[j % key.length].charCodeAt(0) - 65);
            if (c === c.toUpperCase()) {
                result += String.fromCharCode((c.charCodeAt(0) - 65 - offset + 26) % 26 + 65);
            } else {
                result += String.fromCharCode((c.charCodeAt(0) - 97 - offset + 26) % 26 + 97);
            }
            j++;
        } else {
            result += c;
        }
    }
    return result;
}

// Simple 2x2 Hill Cipher implementation
function hillEncrypt(text, key) {
    key = key.replace(/\s+/g, '').toUpperCase();
    if (key.length !== 4) return "Key must be 4 letters";
    let matrix = [
        [key.charCodeAt(0) - 65, key.charCodeAt(1) - 65],
        [key.charCodeAt(2) - 65, key.charCodeAt(3) - 65]
    ];
    text = text.replace(/\s+/g, '').toUpperCase();
    if (text.length % 2 !== 0) text += 'X';
    let result = '';
    for (let i = 0; i < text.length; i += 2) {
        let vector = [text.charCodeAt(i) - 65, text.charCodeAt(i + 1) - 65];
        let resVec = [
            (matrix[0][0] * vector[0] + matrix[0][1] * vector[1]) % 26,
            (matrix[1][0] * vector[0] + matrix[1][1] * vector[1]) % 26
        ];
        result += String.fromCharCode(resVec[0] + 65) + String.fromCharCode(resVec[1] + 65);
    }
    return result;
}

function hillDecrypt(text, key) {
    key = key.replace(/\s+/g, '').toUpperCase();
    if (key.length !== 4) return "Key must be 4 letters";
    let det = (key.charCodeAt(0) - 65) * (key.charCodeAt(3) - 65) -
              (key.charCodeAt(1) - 65) * (key.charCodeAt(2) - 65);
    det = ((det % 26) + 26) % 26;
    let invDet = -1;
    for (let i = 0; i < 26; i++) if ((det * i) % 26 === 1) invDet = i;
    if (invDet === -1) return "Key not invertible";
    let matrix = [
        [key.charCodeAt(0) - 65, key.charCodeAt(1) - 65],
        [key.charCodeAt(2) - 65, key.charCodeAt(3) - 65]
    ];
    let adj = [
        [matrix[1][1], -matrix[0][1]],
        [-matrix[1][0], matrix[0][0]]
    ];
    let invMatrix = [
        [(invDet * ((adj[0][0] % 26 + 26) % 26)) % 26,
         (invDet * ((adj[0][1] % 26 + 26) % 26)) % 26],
        [(invDet * ((adj[1][0] % 26 + 26) % 26)) % 26,
         (invDet * ((adj[1][1] % 26 + 26) % 26)) % 26]
    ];
    text = text.replace(/\s+/g, '').toUpperCase();
    let result = '';
    for (let i = 0; i < text.length; i += 2) {
        let vector = [text.charCodeAt(i) - 65, text.charCodeAt(i + 1) - 65];
        let resVec = [
            (invMatrix[0][0] * vector[0] + invMatrix[0][1] * vector[1]) % 26,
            (invMatrix[1][0] * vector[0] + invMatrix[1][1] * vector[1]) % 26
        ];
        result += String.fromCharCode(resVec[0] + 65) + String.fromCharCode(resVec[1] + 65);
    }
    return result;
}

function encrypt() {
    let text = document.getElementById('text').value;
    let cipher = document.getElementById('cipher').value;
    let key = document.getElementById('key').value;
    let output = "";
    if (cipher === 'caesar') output = caesarShift(text, parseInt(key));
    if (cipher === 'vigenere') output = vigenereEncrypt(text, key);
    if (cipher === 'hill') output = hillEncrypt(text, key);
    document.getElementById('output').innerText = output;
}

function decrypt() {
    let text = document.getElementById('text').value;
    let cipher = document.getElementById('cipher').value;
    let key = document.getElementById('key').value;
    let output = "";
    if (cipher === 'caesar') output = caesarShift(text, -parseInt(key));
    if (cipher === 'vigenere') output = vigenereDecrypt(text, key);
    if (cipher === 'hill') output = hillDecrypt(text, key);
    document.getElementById('output').innerText = output;
}
</script>
</body>
</html>
