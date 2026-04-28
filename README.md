```
 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
 ░                                                                          ░
 ░    █████╗ ███████╗ ██████╗██╗██╗      ██████╗ ███████╗ █████╗ ██╗      ░
 ░   ██╔══██╗██╔════╝██╔════╝██║██║     ██╔══██╗██╔════╝██╔══██╗██║      ░
 ░   ███████║███████╗██║     ██║██║     ██████╔╝█████╗  ███████║██║      ░
 ░   ██╔══██║╚════██║██║     ██║██║     ██╔══██╗██╔══╝  ██╔══██║██║      ░
 ░   ██║  ██║███████║╚██████╗██║███████╗██║  ██║███████╗██║  ██║███████╗ ░
 ░   ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝ ░
 ░                                                                          ░
 ░      ██████╗ ███████╗ █████╗ ██╗     ████████╗██╗███╗   ███╗███████╗   ░
 ░      ██╔══██╗██╔════╝██╔══██╗██║        ██║   ██║████╗ ████║██╔════╝   ░
 ░      ██████╔╝█████╗  ███████║██║        ██║   ██║██╔████╔██║█████╗     ░
 ░      ██╔══██╗██╔══╝  ██╔══██║██║        ██║   ██║██║╚██╔╝██║██╔══╝     ░
 ░      ██║  ██║███████╗██║  ██║███████╗   ██║   ██║██║ ╚═╝ ██║███████╗   ░
 ░      ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝   ░
 ░                                                                          ░
 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
```

> *Your face, rendered in characters. Real-time. In the terminal.*

---

## ▓ What Is This?

**ASCII-Realtime** captures your webcam feed and renders it live in the terminal as ASCII art — with customizable gradients, colors, contrast, gamma correction, and more. No GUI. No browser. Just glorious characters streaming to your shell.

```
 .''^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$
```

---

## ▓ Preview

```
.....,,,;;::--==++**##%%@@@@##**++==--::;;,,,...........,,;;::--
..,,;;::--==++**##%%@@@@@@@@%%##**++==--::;;,,,.....,,;;::--==++
,;;::--==++**##%%@@@@@@@@@@@@@@%%##**++==--::;;,,,,;;::--==++**#
::--==++**##%%@@@@@@@@@@@@@@@@@@@@%%##**++==--::::::--==++**##%%
--==++**##%%@@@@@@@@@@@@@@@@@@@@@@@@%%##**++====++**##%%@@@@@@@@
```

*(actual output will vary — that's kinda the point)*

---

## ▓ Requirements

- Python 3.7+
- A working webcam
- A terminal that supports ANSI colors (most modern ones do)

### Install dependencies

```bash
pip install opencv-python colorama numpy
```

---

## ▓ How to Run

```bash
python main.py
```

Press **`Ctrl+C`** to stop.

That's it. Your webcam feed will start rendering in ASCII in your terminal window.

> 💡 **Tip:** Make your terminal font smaller and window larger for a much better experience. `6–8px` font size works great.

---

## ▓ Configuration

Open `main.py` and tweak these variables at the top:

```python
gradient_name = "detailed"   # "smooth" | "blocks" | "detailed"
color_name    = "green"      # "white" | "green" | "red" | "cyan" | "yellow"

contrast   = 1.5    # float — higher = more contrast
brightness = 0      # int   — positive = brighter, negative = darker
gamma      = 0.8    # float — lower = darker shadows
invert     = False  # True  = white-on-black becomes black-on-white
width      = 120    # int   — character columns (wider = more detail)
```

### Gradient Styles

| Name | Characters Used | Best For |
|---|---|---|
| `smooth` | ` .:-=+*#%@` | Clean, simple look |
| `blocks` | ` ░▒▓█` | Block-style retro feel |
| `detailed` | 70-char set | Maximum detail & contrast |

### Color Modes

| Name | Effect |
|---|---|
| `white` | Default terminal color |
| `green` | Classic matrix green 🟢 |
| `red` | Danger / heat map 🔴 |
| `cyan` | Cool cyber aesthetic 🔵 |
| `yellow` | Warm, vintage terminal 🟡 |

---

## ▓ How It Works

```
Webcam Frame
     │
     ▼
Convert to Grayscale (cv2)
     │
     ▼
Apply Contrast + Brightness
     │
     ▼
Apply Gamma Correction
     │
     ▼
(Optional) Invert
     │
     ▼
Resize → width × (width * aspect * 0.45)
     │
     ▼
Map each pixel → ASCII character
     │
     ▼
Print to terminal with ANSI color
     │
     ▼
Repeat every ~30ms
```

The **0.45 aspect ratio multiplier** corrects for the fact that terminal characters are roughly twice as tall as they are wide — without it, everything would look squished vertically.

---

## ▓ Suggested Improvements

Want to take this further? Here are some ideas:

### 🎨 Visual Enhancements
- **Edge detection mode** — run a Canny filter before ASCII conversion for a sketchy, comic-book outline look
- **Colored ASCII** — map each character's RGB value (not just grayscale) for full-color terminal output using `\033[38;2;R;G;Bm` true color codes
- **Custom gradients** — let users define their own character sets via a config file

### 🖥️ UX / Controls
- **Live hotkeys** — press `g` to cycle gradients, `c` to cycle colors, `+/-` to adjust width, all without restarting
- **FPS display** — show current frames-per-second in the corner
- **Snapshot mode** — press `s` to save the current ASCII frame to a `.txt` file

### 📦 CLI Interface
```bash
python main.py --gradient detailed --color cyan --width 150 --invert
```
Use `argparse` to make all config options passable as flags.

---

## ▓ Project Structure

```
ASCII-Realtime/
├── main.py       # Main script
└── README.md     # You are here
```

---

## ▓ License

Do whatever you want with it. It's terminal art.

---

```
 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
 ░  made with ▓▒░ and Python  ░▒▓  ░
 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
```