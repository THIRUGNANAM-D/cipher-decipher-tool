<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>Majestic Flames Crypto + Stego (All Ciphers)</title>
  <style>
    /* ========== Majestic flames + blue spray background ========== */
    :root{
      --bg:#070707;
      --flame1: #ff6a00;
      --flame2: #ff3b1f;
      --ember:#b71c1c;
      --blue-spray: rgba(35,150,255,0.16);
      --card:#121212;
      --neon:#3fb0ff;
      --accent:#ff2b3b;
      --muted:#bfc7d6;
      --glass: rgba(255,255,255,0.03);
    }
    html,body{height:100%;margin:0;font-family:Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;}
    body{
      background:
        radial-gradient(900px 500px at 10% -20%, rgba(255,90,30,0.06), transparent 26%),
        radial-gradient(800px 400px at 120% 20%, rgba(255,30,60,0.045), transparent 30%),
        linear-gradient(180deg, #050507 0%, #0b0a0b 40%, #0b0606 100%);
      color:var(--muted);
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
      overflow-x:hidden;
    }

    /* spray canvas sits above bg */
    #spray {
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 0;
      mix-blend-mode: screen;
      opacity: 0.85;
      filter: blur(8px) saturate(1.1);
    }

    .page {
      position: relative;
      z-index: 2;
      padding: 28px;
    }

    header { text-align:center; margin-bottom:18px; }
    h1{
      font-size:34px; margin:0; color: #fff;
      text-shadow: 0 0 10px rgba(255,100,70,0.12), 0 0 36px rgba(50,120,255,0.06);
      letter-spacing: 2px;
    }
    p.lead { color:var(--neon); margin:6px 0 18px 0; font-weight:600; }

    /* single-row layout */
    .row {
      display:flex;
      gap:18px;
      align-items:flex-start;
      overflow:auto;
      padding-bottom:12px;
    }
    .card {
      min-width: 360px;
      background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
      border-radius:14px;
      border: 1px solid rgba(255,255,255,0.04);
      box-shadow: 0 12px 28px rgba(3,6,12,0.6), 0 0 28px rgba(50,120,255,0.03);
      padding:16px;
      flex: 0 0 auto;
      z-index: 3;
    }
    .card h2 { margin:0 0 8px 0; color:var(--accent); font-size:18px; }
    label{ display:block; font-size:13px; color:var(--muted); margin-bottom:6px; }
    textarea, input[type="text"], input[type="number"], select {
      width:100%; padding:10px; border-radius:10px; border:1px solid rgba(255,255,255,0.04); background:var(--card); color:#eef2ff; font-size:14px;
      box-sizing:border-box;
    }
    textarea { resize:vertical; min-height:88px; font-family:monospace; }
    .small { font-size:12px; color:#aab6c7; margin-top:6px; }

    .btn {
      display:inline-block; padding:10px 14px; border-radius:10px; margin-top:10px; cursor:pointer;
      font-weight:700; letter-spacing:0.6px; border: none;
    }
    .btn-primary { background: linear-gradient(90deg,var(--accent), #ff6a6a); color:#0b0b0b; box-shadow: 0 8px 22px rgba(255,40,60,0.14); }
    .btn-ghost { background: transparent; color:var(--neon); border:1px solid rgba(255,255,255,0.04); box-shadow:none; }
    .btn-success { background: linear-gradient(90deg,#29b6f6,#3fb0ff); color:#031224; }

    .inline { display:flex; gap:8px; align-items:center; }
    .muted { color:#9fb2cc; font-size:13px; }
    .outbox { background:#0b0b0c; padding:10px; border-radius:10px; min-height:56px; color:#e6f7ff; font-family:monospace; white-space:pre-wrap; word-break:break-word; }

    canvas#stegoCanvas { width:100%; border-radius:10px; display:block; margin-top:10px; border:2px solid rgba(255,255,255,0.04); box-shadow: 0 6px 18px rgba(63,176,255,0.06); background:#000; }

    .footer { margin-top:18px; color:#96a8bf; font-size:13px; text-align:center; }

    /* responsive */
    @media (max-width:980px){
      .card { min-width:300px; }
      h1{ font-size:28px; }
    }
  </style>
</head>
<body>
  <canvas id="spray"></canvas>

  <div class="page">
    <header>
      <h1>Majestic Flames Lab — Crypto + Stego</h1>
      <p class="lead">All ciphers (Caesar, Vigenère, Hill 2×2) + LSB steganography — single row interface</p>
    </header>

    <div class="row">
      <!-- Card 1: Cipher chooser + plaintext -->
      <div class="card" id="card-cipher">
        <h2>Cipher & Plaintext</h2>

        <label>Choose Cipher</label>
        <div class="inline" style="margin-bottom:8px;">
          <select id="cipherSelect">
            <option>Caesar</option>
            <option>Vigenère</option>
            <option>Hill 2x2</option>
          </select>
          <button class="btn btn-ghost" id="swapBtn">Swap ⇄</button>
        </div>

        <label>Plaintext</label>
        <textarea id="plaintext" placeholder="Type your message here..."></textarea>

        <div id="keyArea" style="margin-top:10px;">
          <!-- Caesar -->
          <div id="caesarKey" style="display:block;">
            <label>Caesar shift (0-25)</label>
            <input type="number" id="caesarShift" min="0" max="25" value="3"/>
          </div>
          <!-- Vigenere -->
          <div id="vigenereKey" style="display:none;">
            <label>Vigenère key (alphabetic)</label>
            <input type="text" id="vigenereKeyIn" placeholder="keyword"/>
          </div>
          <!-- Hill -->
          <div id="hillKey" style="display:none;">
            <label>Hill key (a b c d) — 2×2</label>
            <input type="text" id="hillKeyIn" placeholder="5 8 17 3" value="5 8 17 3"/>
            <div class="small">Key must be 4 integers; determinant must be invertible mod 26.</div>
          </div>
        </div>

        <div style="margin-top:12px;" class="inline">
          <button class="btn btn-primary" id="encryptBtn">Encrypt ▶</button>
          <button class="btn btn-ghost" id="clearBtn">Clear</button>
        </div>
      </div>

      <!-- Card 2: Ciphertext & decrypt -->
      <div class="card" id="card-output">
        <h2>Ciphertext & Decrypt</h2>

        <label>Ciphertext</label>
        <textarea id="ciphertext" placeholder="Ciphertext appears here..." readonly></textarea>

        <label style="margin-top:8px;">Decrypt key (match cipher)</label>
        <input type="text" id="decryptKey" placeholder="shift / keyword / a b c d"/>

        <div style="margin-top:10px;" class="inline">
          <button class="btn btn-success" id="decryptBtn">Decrypt ◀</button>
          <button class="btn btn-ghost" id="copyCipher">Copy</button>
        </div>

        <label style="margin-top:12px;">Decrypted Plaintext</label>
        <div class="outbox" id="decryptedOut"></div>
      </div>

      <!-- Card 3: Stego hide/reveal -->
      <div class="card" id="card-stego">
        <h2>Steganography (LSB)</h2>

        <label>Message source</label>
        <div class="inline" style="margin-bottom:8px;">
          <label class="muted"><input type="radio" name="src" value="cipher" checked/> Use Ciphertext</label>
          <label class="muted" style="margin-left:12px;"><input type="radio" name="src" value="custom"/> Custom</label>
        </div>

        <input type="text" id="customMsg" placeholder="Optional custom message..." style="margin-bottom:8px;"/>

        <label>Cover Image</label>
        <input type="file" id="coverFile" accept="image/*"/>

        <div style="margin-top:10px;" class="inline">
          <button class="btn btn-primary" id="hideBtn">Hide ▶</button>
          <button class="btn btn-ghost" id="saveStegoBtn" disabled>Save Stego</button>
        </div>

        <label style="margin-top:12px;">Stego Canvas</label>
        <canvas id="stegoCanvas" width="420" height="280"></canvas>

        <hr style="margin:12px 0; border:none; border-top:1px solid rgba(255,255,255,0.03)"/>

        <label>Reveal from image</label>
        <input type="file" id="revealFile" accept="image/*" style="margin-bottom:8px;"/>

        <div style="margin-top:8px;" class="inline">
          <button class="btn btn-success" id="revealBtn">Reveal ◀</button>
          <button class="btn btn-ghost" id="copyReveal" disabled>Copy</button>
        </div>

        <label style="margin-top:12px;">Revealed message</label>
        <div class="outbox" id="revealedOut"></div>
      </div>
    </div>

    <div class="footer">Made for demo — Majestic Flames theme • All client-side, runs in browser</div>
  </div>

  <script>
  // ------------------ Background blue spray generation ------------------
  (function generateSpray() {
    const c = document.getElementById('spray');
    const dpr = window.devicePixelRatio || 1;
    c.width = innerWidth * dpr;
    c.height = innerHeight * dpr;
    c.style.width = innerWidth + 'px';
    c.style.height = innerHeight + 'px';
    const ctx = c.getContext('2d');
    ctx.scale(dpr,dpr);

    // draw random blue mist dots (like spray)
    for (let i=0;i<900;i++){
      const x = Math.random()*innerWidth;
      const y = Math.random()*innerHeight*0.55;
      const r = Math.random()*3 + 0.5;
      ctx.beginPath();
      ctx.fillStyle = 'rgba(60,160,255,' + (0.02 + Math.random()*0.12) + ')';
      ctx.arc(x,y,r,0,Math.PI*2);
      ctx.fill();
    }
    // soft radial gradient overlay
    const g = ctx.createRadialGradient(innerWidth*0.15, innerHeight*0.05, 20, innerWidth*0.12, innerHeight*0.02, innerWidth*0.8);
    g.addColorStop(0, 'rgba(40,140,255,0.06)');
    g.addColorStop(1, 'rgba(0,0,0,0)');
    ctx.fillStyle = g;
    ctx.fillRect(0,0,innerWidth,innerHeight);
  })();

  // ------------------ Helpers ------------------
  function onlyLettersUpper(s){ return (s||'').replace(/[^a-zA-Z]/g,'').toUpperCase(); }
  function padX(s,n){ while(s.length % n !== 0) s += 'X'; return s; }
  function modInverse(n, m=26){
    n = ((n % m) + m) % m;
    for(let x=1;x<m;x++) if((n*x)%m === 1) return x;
    return null;
  }

  // ------------------ Caesar ------------------
  function caesarEncrypt(plain, shift){
    const p = onlyLettersUpper(plain); shift = ((shift%26)+26)%26;
    return p.split('').map(ch => String.fromCharCode((ch.charCodeAt(0)-65+shift)%26 + 65)).join('');
  }
  function caesarDecrypt(ct, shift){ return caesarEncrypt(ct, -shift); }

  // ------------------ VIGENERE ------------------
  function vigenereEncrypt(plain, key){
    const p = onlyLettersUpper(plain);
    const k = onlyLettersUpper(key);
    if(!k) return '';
    let out='', ki=0;
    for(const ch of p){
      const s = k[ki % k.length].charCodeAt(0)-65;
      out += String.fromCharCode((ch.charCodeAt(0)-65 + s)%26 + 65);
      ki++;
    }
    return out;
  }
  function vigenereDecrypt(ct, key){
    const c = onlyLettersUpper(ct);
    const k = onlyLettersUpper(key);
    if(!k) return '';
    let out='', ki=0;
    for(const ch of c){
      const s = k[ki % k.length].charCodeAt(0)-65;
      out += String.fromCharCode((ch.charCodeAt(0)-65 - s + 26)%26 + 65);
      ki++;
    }
    return out;
  }

  // ------------------ HILL 2x2 ------------------
  function parseHillKey2x2(s){
    try {
      const nums = s.trim().replace(/,/g,' ').split(/\s+/).map(Number);
      if(nums.length !== 4 || nums.some(isNaN)) return null;
      return [[nums[0], nums[1]],[nums[2], nums[3]]];
    } catch(e){ return null; }
  }
  function det2x2(M){ return ((M[0][0]*M[1][1] - M[0][1]*M[1][0])%26 + 26) %26; }
  function invMatrix2x2(M){
    const d = det2x2(M);
    const invd = modInverse(d,26);
    if(invd===null) return null;
    const a=M[0][0], b=M[0][1], c=M[1][0], d0=M[1][1];
    const adj = [[d0, -b],[-c, a]];
    return [[(adj[0][0]*invd)%26, (adj[0][1]*invd)%26],[ (adj[1][0]*invd)%26, (adj[1][1]*invd)%26 ]].map(row=>row.map(v=>((v%26)+26)%26));
  }
  function hillEncrypt2(plain, keyStr){
    const M = parseHillKey2x2(keyStr); if(!M) return '';
    if(modInverse(det2x2(M),26)===null) return '';
    let pt = onlyLettersUpper(plain); pt = padX(pt,2);
    let out='';
    for(let i=0;i<pt.length;i+=2){
      const v0 = pt.charCodeAt(i)-65, v1 = pt.charCodeAt(i+1)-65;
      const c0 = (M[0][0]*v0 + M[0][1]*v1)%26;
      const c1 = (M[1][0]*v0 + M[1][1]*v1)%26;
      out += String.fromCharCode(c0+65) + String.fromCharCode(c1+65);
    }
    return out;
  }
  function hillDecrypt2(ct, keyStr){
    const M = parseHillKey2x2(keyStr); if(!M) return '';
    const Minv = invMatrix2x2(M); if(!Minv) return '';
    const c = onlyLettersUpper(ct);
    if(c.length %2 !==0) return '';
    let out='';
    for(let i=0;i<c.length;i+=2){
      const v0 = c.charCodeAt(i)-65, v1 = c.charCodeAt(i+1)-65;
      const p0 = (Minv[0][0]*v0 + Minv[0][1]*v1)%26;
      const p1 = (Minv[1][0]*v0 + Minv[1][1]*v1)%26;
      out += String.fromCharCode((p0+26)%26 + 65) + String.fromCharCode((p1+26)%26 + 65);
    }
    return out;
  }

  // ------------------ LSB stego (canvas) ------------------
  function textToBits(s){
    return Array.from(s).map(c => c.charCodeAt(0).toString(2).padStart(8,'0')).join('');
  }
  function bitsToText(bits){
    let out='';
    for(let i=0;i<bits.length;i+=8){
      const byte = bits.slice(i,i+8);
      if(byte.length<8) break;
      out += String.fromCharCode(parseInt(byte,2));
    }
    return out;
  }

  function hideMessageInCanvas(img, message, canvas){
    // img: HTMLImageElement or ImageBitmap. canvas: target canvas element (2D)
    const ctx = canvas.getContext('2d');
    canvas.width = img.width;
    canvas.height = img.height;
    ctx.drawImage(img,0,0);
    const imageData = ctx.getImageData(0,0,canvas.width, canvas.height);
    const data = imageData.data; // RGBA
    const bits = textToBits(message);
    const L = bits.length;
    const lenBits = L.toString(2).padStart(32,'0');
    const total = 32 + L;
    if(total > data.length) throw new Error('Image too small to hide message.');
    // write length first (first 32 LSBs)
    let bi = 0;
    for(let i=0;i<32;i++){
      const byteIdx = i;
      data[byteIdx] = (data[byteIdx] & 0xFE) | Number(lenBits[i]);
    }
    bi = 0;
    for(let i=32;i<data.length && bi < L; i++){
      data[i] = (data[i] & 0xFE) | Number(bits[bi]);
      bi++;
    }
    ctx.putImageData(imageData,0,0);
    return canvas;
  }

  function revealMessageFromCanvas(img, canvas){
    const ctx = canvas.getContext('2d');
    canvas.width = img.width; canvas.height = img.height;
    ctx.drawImage(img,0,0);
    const imageData = ctx.getImageData(0,0,canvas.width, canvas.height);
    const data = imageData.data;
    let lenBits='';
    for(let i=0;i<32;i++) lenBits += (data[i] & 1).toString();
    const L = parseInt(lenBits,2);
    let bits = '';
    for(let i=32;i<32+L && i<data.length;i++) bits += (data[i] & 1).toString();
    return bitsToText(bits);
  }

  // ------------------ DOM wiring ------------------
  const cipherSelect = document.getElementById('cipherSelect');
  const plaintext = document.getElementById('plaintext');
  const caesarShift = document.getElementById('caesarShift');
  const vigenereKeyIn = document.getElementById('vigenereKeyIn');
  const hillKeyIn = document.getElementById('hillKeyIn');

  const encryptBtn = document.getElementById('encryptBtn');
  const clearBtn = document.getElementById('clearBtn');
  const ciphertext = document.getElementById('ciphertext');
  const decryptBtn = document.getElementById('decryptBtn');
  const decryptKey = document.getElementById('decryptKey');
  const decryptedOut = document.getElementById('decryptedOut');
  const copyCipher = document.getElementById('copyCipher');

  const coverFile = document.getElementById('coverFile');
  const hideBtn = document.getElementById('hideBtn');
  const saveStegoBtn = document.getElementById('saveStegoBtn');
  const stCanvas = document.getElementById('stegoCanvas');
  const revealFile = document.getElementById('revealFile');
  const revealBtn = document.getElementById('revealBtn');
  const revealedOut = document.getElementById('revealedOut');
  const customMsg = document.getElementById('customMsg');
  const srcRadios = document.getElementsByName('src');
  const copyReveal = document.getElementById('copyReveal');

  const caesarKeyDiv = document.getElementById('caesarKey');
  const vigenereKeyDiv = document.getElementById('vigenereKey');
  const hillKeyDiv = document.getElementById('hillKey');

  const swapBtn = document.getElementById('swapBtn');

  function showKeyArea(){
    const val = cipherSelect.value;
    caesarKeyDiv.style.display = val==='Caesar' ? 'block':'none';
    vigenereKeyDiv.style.display = val==='Vigenère' ? 'block':'none';
    hillKeyDiv.style.display = val==='Hill 2x2' ? 'block':'none';
  }
  cipherSelect.addEventListener('change', showKeyArea);
  showKeyArea();

  swapBtn.addEventListener('click', ()=>{
    // swap ciphertext <-> plaintext
    const p = plaintext.value;
    const c = ciphertext.value;
    plaintext.value = c;
    ciphertext.value = p;
  });

  encryptBtn.addEventListener('click', ()=>{
    const mode = cipherSelect.value;
    const pt = plaintext.value || '';
    let ct = '';
    try {
      if(mode === 'Caesar'){
        const s = Number(caesarShift.value) || 0;
        ct = caesarEncrypt(pt, s);
      } else if(mode === 'Vigenère'){
        const k = vigenereKeyIn.value || '';
        if(!k.trim()) return alert('Provide Vigenère key.');
        ct = vigenereEncrypt(pt, k);
      } else {
        const k = hillKeyIn.value || '';
        if(!parseHillKey2x2(k)) return alert('Hill key must be 4 integers (a b c d).');
        ct = hillEncrypt2(pt, k);
        if(!ct) return alert('Hill key invalid (determinant not invertible mod 26).');
      }
      ciphertext.value = ct;
      // prefill decrypt key
      if(mode==='Caesar') decryptKey.value = caesarShift.value;
      else if(mode==='Vigenère') decryptKey.value = vigenereKeyIn.value;
      else decryptKey.value = hillKeyIn.value;
    } catch(e){ alert('Encryption failed: '+e.message); }
  });

  clearBtn.addEventListener('click', ()=>{
    plaintext.value = ''; ciphertext.value = ''; decryptKey.value=''; decryptedOut.textContent=''; revealedOut.textContent='';
  });

  decryptBtn.addEventListener('click', ()=>{
    const mode = cipherSelect.value;
    const ct = ciphertext.value || '';
    const key = decryptKey.value || '';
    let pt = '';
    try{
      if(mode==='Caesar'){
        const s = Number(key);
        if(isNaN(s)) return alert('Decrypt key for Caesar must be integer.');
        pt = caesarDecrypt(ct, s);
      } else if(mode==='Vigenère'){
        if(!key.trim()) return alert('Provide Vigenère key to decrypt.');
        pt = vigenereDecrypt(ct, key);
      } else {
        if(!parseHillKey2x2(key)) return alert('Hill decrypt key must be 4 ints.');
        pt = hillDecrypt2(ct, key);
        if(!pt) return alert('Invalid Hill key or ciphertext length.');
      }
      decryptedOut.textContent = pt;
    }catch(e){ alert('Decryption failed: '+e.message); }
  });

  copyCipher.addEventListener('click', ()=>{
    navigator.clipboard.writeText(ciphertext.value).then(()=>alert('Ciphertext copied.'));
  });

  // ------------------ Stego file handling ------------------
  let coverImage = null;
  coverFile.addEventListener('change', (ev)=>{
    const f = ev.target.files[0];
    if(!f) return;
    const img = new Image();
    img.onload = ()=>{ coverImage = img; alert('Cover image loaded: '+img.width+'×'+img.height); };
    img.onerror = ()=>alert('Failed to load image.');
    const url = URL.createObjectURL(f);
    img.src = url;
  });

  hideBtn.addEventListener('click', ()=>{
    if(!coverImage) return alert('Load cover image first.');
    let msgSource = document.querySelector('input[name="src"]:checked').value;
    let message = msgSource === 'cipher' ? (ciphertext.value || '') : (customMsg.value || '');
    if(!message) return alert('Nothing to hide. Provide ciphertext or custom message.');
    try {
      hideMessageInCanvas(coverImage, message, stCanvas);
      saveStegoBtn.disabled = false;
      alert('Message hidden on canvas. Click Save Stego to download.');
    } catch(e){ alert('Hiding failed: '+e.message); }
  });

  saveStegoBtn.addEventListener('click', ()=>{
    const a = document.createElement('a');
    a.href = stCanvas.toDataURL('image/png');
    a.download = 'stego.png';
    a.click();
  });

  revealBtn.addEventListener('click', ()=>{
    const f = revealFile.files[0];
    if(!f) return alert('Choose an image to reveal from.');
    const img = new Image();
    img.onload = ()=>{
      try {
        const result = revealMessageFromCanvas(img, stCanvas);
        revealedOut.textContent = result || '[No hidden message found]';
        copyReveal.disabled = !result;
      } catch(e){ alert('Reveal failed: '+e.message); }
    };
    img.onerror = ()=>alert('Failed to load reveal image.');
    img.src = URL.createObjectURL(f);
  });

  copyReveal.addEventListener('click', ()=> {
    const txt = revealedOut.textContent || '';
    navigator.clipboard.writeText(txt).then(()=>alert('Revealed message copied.'));
  });

  // small UX: if user switches source, clear custom
  Array.from(srcRadios).forEach(r=>r.addEventListener('change', ()=>{ if(r.value==='custom' && r.checked) customMsg.focus(); }));

  // init: show area
  showKeyArea();
  </script>
</body>
</html>
