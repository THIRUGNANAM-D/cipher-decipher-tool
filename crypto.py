# majestic_crypto_stego_gui.py
# GUI: Tkinter + PIL
# Ciphers: Caesar, Vigenère, Hill(2x2)  + LSB Steganography
# Theme: "Majestic Flames" background with a hint of blue spray

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw
import io
import math

# ---------------------- THEME / BACKGROUND ----------------------
def create_flame_bg(width=1600, height=700):
    """
    Create a dynamic 'majestic flames + blue spray' background.
    - Bottom: fiery gradient (dark -> deep red -> orange -> gold)
    - Top overlay: soft blue spray mist
    """
    img = Image.new("RGB", (width, height), "#0a0a0a")
    draw = ImageDraw.Draw(img)

    # vertical gradient (flame tones)
    # stops from bottom to top
    stops = [
        (0.00, (250, 95, 0)),     # orange
        (0.20, (255, 140, 0)),    # orange-gold
        (0.45, (200, 40, 10)),    # deep ember
        (0.70, (30, 10, 10)),     # dark
        (1.00, (10, 10, 12)),     # very dark
    ]
    for y in range(height):
        t = 1 - y / (height - 1)
        # find surrounding color stops
        lower = max([s for s in stops if s[0] <= t], key=lambda s: s[0])
        upper = min([s for s in stops if s[0] >= t], key=lambda s: s[0])
        if lower[0] == upper[0]:
            r, g, b = lower[1]
        else:
            u = (t - lower[0]) / (upper[0] - lower[0])
            r = int(lower[1][0] * (1 - u) + upper[1][0] * u)
            g = int(lower[1][1] * (1 - u) + upper[1][1] * u)
            b = int(lower[1][2] * (1 - u) + upper[1][2] * u)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # add subtle flame streaks
    for x in range(0, width, 40):
        for y in range(height - 200, height, 4):
            alpha = int(60 * (1 - (height - y) / 200))
            col = (255, 120, 40)
            draw.line([(x, y), (x + 12, y - 20)], fill=col, width=1)

    # blue spray mist (light random dots/blur-like)
    import random
    spray = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(spray)
    for _ in range(600):
        rx = random.randint(0, width - 1)
        ry = random.randint(0, int(height * 0.55))
        rad = random.randint(1, 3)
        sdraw.ellipse((rx - rad, ry - rad, rx + rad, ry + rad),
                      fill=(30, 120, 255, random.randint(35, 75)))
    img = Image.alpha_composite(img.convert("RGBA"), spray).convert("RGB")
    return img

# ---------------------- TEXT HELPERS ----------------------
def only_letters_up(text):
    return ''.join([c for c in text if c.isalpha()]).upper()

def pad_x(text, size):
    while len(text) % size != 0:
        text += 'X'
    return text

# ---------------------- CAESAR ----------------------
def caesar_encrypt(plaintext, shift):
    pt = only_letters_up(plaintext)
    shift %= 26
    out = []
    for ch in pt:
        out.append(chr(((ord(ch) - 65 + shift) % 26) + 65))
    return ''.join(out)

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

# ---------------------- VIGENERE ----------------------
def vigenere_encrypt(plaintext, key):
    pt = only_letters_up(plaintext)
    k = only_letters_up(key)
    if not k:
        return ""
    out = []
    ki = 0
    for ch in pt:
        s = ord(k[ki % len(k)]) - 65
        out.append(chr(((ord(ch) - 65 + s) % 26) + 65))
        ki += 1
    return ''.join(out)

def vigenere_decrypt(ciphertext, key):
    ct = only_letters_up(ciphertext)
    k = only_letters_up(key)
    if not k:
        return ""
    out = []
    ki = 0
    for ch in ct:
        s = ord(k[ki % len(k)]) - 65
        out.append(chr(((ord(ch) - 65 - s) % 26) + 65))
        ki += 1
    return ''.join(out)

# ---------------------- HILL 2x2 ----------------------
MOD = 26

def mod_inv(a, m=MOD):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def parse_hill_key_2x2(s):
    try:
        nums = [int(x) for x in s.strip().replace(',', ' ').split()]
        if len(nums) != 4:
            return None
        return [[nums[0], nums[1]], [nums[2], nums[3]]]
    except:
        return None

def det_2x2(M):
    return (M[0][0] * M[1][1] - M[0][1] * M[1][0]) % MOD

def inv_matrix_2x2(M):
    d = det_2x2(M)
    invd = mod_inv(d, MOD)
    if invd is None:
        return None
    # adjugate
    a, b, c, d0 = M[0][0], M[0][1], M[1][0], M[1][1]
    adj = [[d0, -b],
           [-c, a]]
    inv = [[(adj[i][j] * invd) % MOD for j in range(2)] for i in range(2)]
    return inv

def hill2_encrypt(plaintext, key_str):
    M = parse_hill_key_2x2(key_str)
    if M is None:
        return ""
    if mod_inv(det_2x2(M), MOD) is None:
        return ""
    pt = pad_x(only_letters_up(plaintext), 2)
    out = []
    for i in range(0, len(pt), 2):
        v = [ord(pt[i]) - 65, ord(pt[i+1]) - 65]
        c0 = (M[0][0] * v[0] + M[0][1] * v[1]) % MOD
        c1 = (M[1][0] * v[0] + M[1][1] * v[1]) % MOD
        out.append(chr(c0 + 65))
        out.append(chr(c1 + 65))
    return ''.join(out)

def hill2_decrypt(ciphertext, key_str):
    M = parse_hill_key_2x2(key_str)
    if M is None:
        return ""
    Minv = inv_matrix_2x2(M)
    if Minv is None:
        return ""
    ct = only_letters_up(ciphertext)
    if len(ct) % 2 != 0:
        return ""
    out = []
    for i in range(0, len(ct), 2):
        v = [ord(ct[i]) - 65, ord(ct[i+1]) - 65]
        p0 = (Minv[0][0] * v[0] + Minv[0][1] * v[1]) % MOD
        p1 = (Minv[1][0] * v[0] + Minv[1][1] * v[1]) % MOD
        out.append(chr(p0 + 65))
        out.append(chr(p1 + 65))
    return ''.join(out)

# ---------------------- LSB STEGANOGRAPHY ----------------------
def text_to_bits(s):
    return ''.join(f"{ord(c):08b}" for c in s)

def bits_to_text(bits):
    out = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) < 8:
            break
        out.append(chr(int(byte, 2)))
    return ''.join(out)

def hide_message_in_image(img: Image.Image, message: str) -> Image.Image:
    """
    Store message length (in bits) in first 32 bytes (LSB), then message bits.
    Iterate over all channels (R,G,B,A?) where available.
    """
    if img.mode not in ("RGB", "RGBA"):
        img = img.convert("RGBA")

    pixels = img.load()
    w, h = img.size
    channels = 4 if img.mode == "RGBA" else 3

    msg_bits = text_to_bits(message)
    L = len(msg_bits)
    len_bits = f"{L:032b}"
    total_bits = 32 + L

    if total_bits > w * h * channels:
        raise ValueError("Image too small to hide message.")

    def set_lsb(val, bit):
        return (val & 0xFE) | int(bit)

    bi = 0
    # write length first
    for y in range(h):
        for x in range(w):
            if bi >= total_bits:
                return img
            px = list(pixels[x, y])
            for c in range(channels):
                bit = None
                if bi < 32:
                    bit = len_bits[bi]
                else:
                    bit = msg_bits[bi - 32]
                px[c] = set_lsb(px[c], bit)
                bi += 1
                if bi >= total_bits:
                    break
            pixels[x, y] = tuple(px)
            if bi >= total_bits:
                return img
    return img

def reveal_message_from_image(img: Image.Image) -> str:
    if img.mode not in ("RGB", "RGBA"):
        img = img.convert("RGBA")
    pixels = img.load()
    w, h = img.size
    channels = 4 if img.mode == "RGBA" else 3

    bits = []
    # read first 32 bits (length)
    bi = 0
    len_bits = ""
    for y in range(h):
        for x in range(w):
            px = pixels[x, y]
            for c in range(channels):
                bit = str(px[c] & 1)
                if bi < 32:
                    len_bits += bit
                    bi += 1
                    if bi == 32:
                        L = int(len_bits, 2)
                        # read L bits now
                        msg_bits = []
                        bj = 0
                        yy, xx, cc = y, x, c + 1
                        while bj < L:
                            if cc >= channels:
                                cc = 0
                                xx += 1
                                if xx >= w:
                                    xx = 0
                                    yy += 1
                                    if yy >= h:
                                        break
                            b = str(pixels[xx, yy][cc] & 1)
                            msg_bits.append(b)
                            cc += 1
                            bj += 1
                        return bits_to_text(''.join(msg_bits))
    return ""

# ---------------------- GUI ----------------------
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("The Blue Sky Lab — Majestic Flames (All Ciphers + Stego)")
        self.geometry("1400x720")
        self.minsize(1200, 640)

        # background image
        self.bg_img = ImageTk.PhotoImage(create_flame_bg(1800, 900))
        self.bg_label = tk.Label(self, image=self.bg_img)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # main horizontal container (single row)
        outer = tk.Frame(self, bg="#00000000")
        outer.pack(fill="both", expand=True, padx=18, pady=18)

        # enable horizontal scroll if window is small
        canvas = tk.Canvas(outer, highlightthickness=0, bg="#00000000")
        hscroll = ttk.Scrollbar(outer, orient="horizontal", command=canvas.xview)
        self.inner = tk.Frame(canvas, bg="#00000000")

        self.inner.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=self.inner, anchor="nw")
        canvas.configure(xscrollcommand=hscroll.set)

        canvas.pack(side="top", fill="both", expand=True)
        hscroll.pack(side="bottom", fill="x")

        # styles
        self.card_bg = "#141417"
        self.neon_border = "#ff1744"
        self.text_fg = "#f1f1f1"
        self.sub_fg = "#a6bfff"

        # build three cards in a single row
        self.build_cipher_card()
        self.build_encrypt_decrypt_card()
        self.build_stego_card()

        # current cipher mode
        self.cipher_var.set("Caesar")

    def make_card(self, parent, title):
        card = tk.Frame(parent, bg=self.card_bg, bd=0, highlightthickness=2, highlightbackground=self.neon_border)
        title_lbl = tk.Label(card, text=title, bg=self.card_bg, fg=self.text_fg, font=("Courier Prime", 14, "bold"))
        title_lbl.pack(anchor="w", padx=14, pady=(12, 6))
        sep = ttk.Separator(card, orient="horizontal")
        sep.pack(fill="x", padx=12, pady=(0, 10))
        return card

    def neon_btn(self, parent, text, cmd, primary=True):
        bg = "#ff1744" if primary else "#2a2a2a"
        fg = "#0b0b0b" if primary else "#ffffff"
        btn = tk.Button(parent, text=text, command=cmd, bg=bg, fg=fg, activebackground="#ff4d6d",
                        activeforeground="#0b0b0b", bd=0, padx=12, pady=8,
                        font=("Courier Prime", 10, "bold"))
        return btn

    # ----- Card 1: Cipher & Inputs -----
    def build_cipher_card(self):
        card = self.make_card(self.inner, "Cipher Settings")
        card.pack(side="left", fill="y", padx=(0, 16), pady=6)

        # cipher selector
        self.cipher_var = tk.StringVar(value="Caesar")
        row1 = tk.Frame(card, bg=self.card_bg)
        row1.pack(fill="x", padx=14, pady=6)

        for name in ["Caesar", "Vigenère", "Hill 2x2"]:
            rb = tk.Radiobutton(row1, text=name, variable=self.cipher_var, value=name,
                                bg=self.card_bg, fg=self.sub_fg, selectcolor=self.card_bg,
                                activebackground=self.card_bg, activeforeground=self.text_fg,
                                font=("Courier Prime", 10, "bold"),
                                command=self.on_cipher_change)
            rb.pack(side="left", padx=8)

        # inputs
        frm = tk.Frame(card, bg=self.card_bg)
        frm.pack(fill="x", padx=14, pady=(6, 2))

        tk.Label(frm, text="Plaintext:", bg=self.card_bg, fg=self.text_fg).grid(row=0, column=0, sticky="w")
        self.pt_entry = tk.Text(frm, height=5, width=36, bg="#0f0f10", fg=self.text_fg, insertbackground=self.text_fg)
        self.pt_entry.grid(row=1, column=0, columnspan=3, sticky="we", pady=(2, 8))

        # Caesar key
        self.cz_label = tk.Label(frm, text="Caesar Shift (0–25):", bg=self.card_bg, fg=self.text_fg)
        self.cz_key = tk.Spinbox(frm, from_=0, to=25, width=6, bg="#0f0f10", fg=self.text_fg, insertbackground=self.text_fg)
        # Vigenère key
        self.vg_label = tk.Label(frm, text="Vigenère Key:", bg=self.card_bg, fg=self.text_fg)
        self.vg_key = tk.Entry(frm, width=16, bg="#0f0f10", fg=self.text_fg, insertbackground=self.text_fg)
        # Hill key
        self.hl_label = tk.Label(frm, text="Hill Key 2x2 (a b c d):", bg=self.card_bg, fg=self.text_fg)
        self.hl_key = tk.Entry(frm, width=18, bg="#0f0f10", fg=self.text_fg, insertbackground=self.text_fg)
        self.hl_key.insert(0, "5 8 17 3")

        # place default (Caesar visible)
        self.cz_label.grid(row=2, column=0, sticky="w", pady=(4, 0))
        self.cz_key.grid(row=2, column=1, sticky="w", padx=(8, 0), pady=(4, 0))

        self.vg_label.grid_forget(); self.vg_key.grid_forget()
        self.hl_label.grid_forget(); self.hl_key.grid_forget()

        btns = tk.Frame(card, bg=self.card_bg)
        btns.pack(fill="x", padx=14, pady=10)
        self.encrypt_btn = self.neon_btn(btns, "Encrypt ▶", self.handle_encrypt, primary=True)
        self.encrypt_btn.pack(side="left")
        self.clear_btn = self.neon_btn(btns, "Clear", self.handle_clear, primary=False)
        self.clear_btn.pack(side="left", padx=8)

    def on_cipher_change(self):
        # toggle key inputs by chosen cipher
        choice = self.cipher_var.get()
        # hide all
        for w in (self.cz_label, self.cz_key, self.vg_label, self.vg_key, self.hl_label, self.hl_key):
            w.grid_forget()

        # show relevant
        frm = self.cz_label.master
        if choice == "Caesar":
            self.cz_label.grid(row=2, column=0, sticky="w", pady=(4, 0))
            self.cz_key.grid(row=2, column=1, sticky="w", padx=(8, 0), pady=(4, 0))
        elif choice == "Vigenère":
            self.vg_label.grid(row=2, column=0, sticky="w", pady=(4, 0))
            self.vg_key.grid(row=2, column=1, sticky="w", padx=(8, 0), pady=(4, 0))
        else:  # Hill 2x2
            self.hl_label.grid(row=2, column=0, sticky="w", pady=(4, 0))
            self.hl_key.grid(row=2, column=1, sticky="w", padx=(8, 0), pady=(4, 0))

    # ----- Card 2: Cipher Output & Decrypt -----
    def build_encrypt_decrypt_card(self):
        card = self.make_card(self.inner, "Cipher Output / Decrypt")
        card.pack(side="left", fill="y", padx=16, pady=6)

        frm = tk.Frame(card, bg=self.card_bg)
        frm.pack(fill="both", expand=True, padx=14, pady=(6, 2))

        # encrypted text
        tk.Label(frm, text="Ciphertext:", bg=self.card_bg, fg=self.text_fg).grid(row=0, column=0, sticky="w")
        self.ct_entry = tk.Text(frm, height=5, width=36, bg="#0f0f10", fg=self.text_fg, insertbackground=self.text_fg)
        self.ct_entry.grid(row=1, column=0, columnspan=3, sticky="we", pady=(2, 8))

        # decrypt inputs
        tk.Label(frm, text="Decrypt Key:", bg=self.card_bg, fg=self.text_fg).grid(row=2, column=0, sticky="w")
        self.dec_key = tk.Entry(frm, width=18, bg="#0f0f10", fg=self.text_fg, insertbackground=self.text_fg)
        self.dec_key.grid(row=2, column=1, sticky="w", padx=(8,0))

        self.decrypt_btn = self.neon_btn(frm, "Decrypt ◀", self.handle_decrypt, primary=False)
        self.decrypt_btn.grid(row=2, column=2, sticky="w", padx=(10, 0))

        # decrypted/plaintext display
        tk.Label(frm, text="Decrypted Plaintext:", bg=self.card_bg, fg=self.text_fg).grid(row=3, column=0, sticky="w", pady=(10, 0))
        self.dec_out = tk.Text(frm, height=5, width=36, bg="#0f0f10", fg=self.text_fg, insertbackground=self.text_fg)
        self.dec_out.grid(row=4, column=0, columnspan=3, sticky="we", pady=(2, 8))

        # tip label
        tip = tk.Label(card, text="Tip: Decrypt key format matches the chosen cipher (shift / keyword / 2x2).",
                       bg=self.card_bg, fg=self.sub_fg, font=("Courier Prime", 9))
        tip.pack(anchor="w", padx=14, pady=(0, 10))

    # ----- Card 3: Steganography -----
    def build_stego_card(self):
        card = self.make_card(self.inner, "Steganography (LSB)")
        card.pack(side="left", fill="both", padx=16, pady=6)

        frm = tk.Frame(card, bg=self.card_bg)
        frm.pack(fill="x", padx=14, pady=(6, 2))

        # Message source: from ciphertext box or custom
        self.msg_source = tk.StringVar(value="cipher")
        row = tk.Frame(frm, bg=self.card_bg)
        row.pack(anchor="w", pady=(0, 6))
        tk.Radiobutton(row, text="Use Ciphertext", variable=self.msg_source, value="cipher",
                       bg=self.card_bg, fg=self.sub_fg, selectcolor=self.card_bg).pack(side="left")
        tk.Radiobutton(row, text="Use Custom Text", variable=self.msg_source, value="custom",
                       bg=self.card_bg, fg=self.sub_fg, selectcolor=self.card_bg).pack(side="left", padx=10)

        self.custom_msg = tk.Entry(frm, width=36, bg="#0f0f10", fg=self.text_fg, insertbackground=self.text_fg)
        self.custom_msg.insert(0, "Optional custom message to hide...")
        self.custom_msg.pack(fill="x", pady=(0, 10))

        # buttons
        btns = tk.Frame(frm, bg=self.card_bg)
        btns.pack(fill="x", pady=(0, 6))
        self.load_img_btn = self.neon_btn(btns, "Load Image", self.load_image, primary=False)
        self.load_img_btn.pack(side="left")
        self.hide_btn = self.neon_btn(btns, "Hide ▶", self.hide_message, primary=True)
        self.hide_btn.pack(side="left", padx=8)
        self.save_img_btn = self.neon_btn(btns, "Save Stego", self.save_stego, primary=False)
        self.save_img_btn.pack(side="left", padx=8)

        # Reveal
        rlbl = tk.Label(frm, text="Reveal from Image:", bg=self.card_bg, fg=self.text_fg)
        rlbl.pack(anchor="w", pady=(8, 2))
        rbtns = tk.Frame(frm, bg=self.card_bg)
        rbtns.pack(fill="x")
        self.load_stego_btn = self.neon_btn(rbtns, "Load Stego Image", self.load_stego, primary=False)
        self.load_stego_btn.pack(side="left")
        self.reveal_btn = self.neon_btn(rbtns, "Reveal ◀", self.reveal_message, primary=True)
        self.reveal_btn.pack(side="left", padx=8)

        tk.Label(frm, text="Revealed Message:", bg=self.card_bg, fg=self.text_fg).pack(anchor="w", pady=(10, 2))
        self.reveal_out = tk.Text(frm, height=6, width=40, bg="#0f0f10", fg=self.text_fg, insertbackground=self.text_fg)
        self.reveal_out.pack(fill="x", pady=(0, 10))

        # image caches
        self.cover_img = None
        self.stego_img = None
        self.reveal_img = None

    # ---------------------- EVENTS ----------------------
    def handle_clear(self):
        self.pt_entry.delete("1.0", "end")
        self.ct_entry.delete("1.0", "end")
        self.dec_key.delete(0, "end")
        self.dec_out.delete("1.0", "end")

    def handle_encrypt(self):
        choice = self.cipher_var.get()
        pt = self.pt_entry.get("1.0", "end").strip()

        if choice == "Caesar":
            try:
                shift = int(self.cz_key.get())
            except ValueError:
                messagebox.showerror("Error", "Caesar shift must be an integer.")
                return
            ct = caesar_encrypt(pt, shift)

        elif choice == "Vigenère":
            key = self.vg_key.get().strip()
            if not key:
                messagebox.showerror("Error", "Vigenère key cannot be empty.")
                return
            ct = vigenere_encrypt(pt, key)

        else:  # Hill 2x2
            key = self.hl_key.get().strip()
            if parse_hill_key_2x2(key) is None:
                messagebox.showerror("Error", "Hill key must be four integers: a b c d.")
                return
            ct = hill2_encrypt(pt, key)
            if not ct:
                messagebox.showerror("Error", "Hill key is not invertible mod 26.")
                return

        self.ct_entry.delete("1.0", "end")
        self.ct_entry.insert("1.0", ct)

        # prefill decrypt key for convenience
        if choice == "Caesar":
            self.dec_key.delete(0, "end")
            self.dec_key.insert(0, self.cz_key.get())
        elif choice == "Vigenère":
            self.dec_key.delete(0, "end")
            self.dec_key.insert(0, self.vg_key.get())
        else:
            self.dec_key.delete(0, "end")
            self.dec_key.insert(0, self.hl_key.get())

    def handle_decrypt(self):
        choice = self.cipher_var.get()
        ct = self.ct_entry.get("1.0", "end").strip()
        key = self.dec_key.get().strip()

        if choice == "Caesar":
            try:
                shift = int(key)
            except ValueError:
                messagebox.showerror("Error", "Caesar decrypt key must be integer shift.")
                return
            pt = caesar_decrypt(ct, shift)

        elif choice == "Vigenère":
            if not key:
                messagebox.showerror("Error", "Vigenère decrypt key cannot be empty.")
                return
            pt = vigenere_decrypt(ct, key)

        else:  # Hill 2x2
            if parse_hill_key_2x2(key) is None:
                messagebox.showerror("Error", "Hill decrypt key must be four integers: a b c d.")
                return
            pt = hill2_decrypt(ct, key)
            if not pt:
                messagebox.showerror("Error", "Invalid/non-invertible Hill key or ciphertext length.")
                return

        self.dec_out.delete("1.0", "end")
        self.dec_out.insert("1.0", pt)

    # ---- Stego handlers
    def load_image(self):
        path = filedialog.askopenfilename(title="Choose Cover Image",
                                          filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.bmp")])
        if not path:
            return
        try:
            self.cover_img = Image.open(path).convert("RGBA")
            messagebox.showinfo("Loaded", f"Cover image loaded: {self.cover_img.size[0]}×{self.cover_img.size[1]}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image:\n{e}")

    def hide_message(self):
        if self.cover_img is None:
            messagebox.showwarning("No Image", "Load a cover image first.")
            return

        message = ""
        if self.msg_source.get() == "cipher":
            message = self.ct_entry.get("1.0", "end").strip()
        else:
            message = self.custom_msg.get().strip()

        if not message:
            messagebox.showwarning("Empty", "Nothing to hide. Provide ciphertext or custom text.")
            return

        try:
            self.stego_img = hide_message_in_image(self.cover_img.copy(), message)
            messagebox.showinfo("Done", "Message hidden inside image. Use 'Save Stego' to export.")
        except Exception as e:
            messagebox.showerror("Error", f"Hiding failed:\n{e}")

    def save_stego(self):
        if self.stego_img is None:
            messagebox.showwarning("No Stego", "No stego image to save. Hide a message first.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".png",
                                            filetypes=[("PNG", "*.png")],
                                            title="Save Stego Image")
        if not path:
            return
        try:
            self.stego_img.save(path, format="PNG")
            messagebox.showinfo("Saved", "Stego image saved.")
        except Exception as e:
            messagebox.showerror("Error", f"Saving failed:\n{e}")

    def load_stego(self):
        path = filedialog.askopenfilename(title="Choose Stego Image",
                                          filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.bmp")])
        if not path:
            return
        try:
            self.reveal_img = Image.open(path)
            messagebox.showinfo("Loaded", f"Stego image loaded.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image:\n{e}")

    def reveal_message(self):
        if self.reveal_img is None:
            messagebox.showwarning("No Image", "Load a stego image first.")
            return
        try:
            msg = reveal_message_from_image(self.reveal_img.copy())
            self.reveal_out.delete("1.0", "end")
            self.reveal_out.insert("1.0", msg)
        except Exception as e:
            messagebox.showerror("Error", f"Reveal failed:\n{e}")


if __name__ == "__main__":
    app = App()
    app.mainloop()
