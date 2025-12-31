# 🛡️ Promon Shield String Deobfuscator

A fast and practical tool to **decrypt string obfuscation used by Promon Shield–protected Android apps**, making static analysis significantly easier.

This tool works by **parsing smali opcode patterns** and **reconstructing runtime string logic**, allowing decryption of both **static and dynamically passed strings**.

---

## ✨ Features

- 🚀 **10x+ faster** than earlier versions (heavily optimized)
- 🔓 Decrypts **`String.intern()`-based obfuscation**
- 🧠 Handles **runtime / dynamically passed strings**
- 📦 Works directly on **APK files**


---

## 🧩 How It Works

1. Uses **apktool** to decompile APK into smali
2. Scans smali for known **Promon Shield string patterns**
3. Reconstructs string logic using Python
4. Replaces encrypted strings with decrypted constants
5. Rebuilds the APK using apktool


---

## 📦 Requirements

- Python **3.8+**
- Java **8+** (required for apktool)

You must download [**apktool JAR**](https://github.com/iBotPeaches/Apktool/releases) and place it **in the same folder as the script**.

⚠️ **Important**:  
&nbsp;&nbsp;&nbsp;&nbsp;The jar **must be in the same directory** as `main.py`.


---

Install dependencies:
```bash
pip install -r requirements.txt
````

---

## 🚀 Usage

### Simply use

```bash
python main.py -a target.apk -o deobfuscated.apk
```

### Help

```
python main.py --help
```

---


## 🧠 Why?

> Just because I couldn’t bypass Frida detection and decided to do this instead 😄<br>
> I'm a noobie script kiddie :(

---

## 🧪 Use Cases

* Reverse engineering Promon-protected apps
* Static analysis without runtime instrumentation
* Understanding app logic hidden behind encrypted strings
* Malware research / security analysis

---

## ⚠️ Disclaimer

This project is intended **for educational and research purposes only**.
Use it only on apps you own or have permission to analyze.

---

## 🤝 Contributing

Contributions are welcome!

If you discover:

* New string patterns
* New opcode flows
* Performance improvements

Please submit a PR 🙏
ILY <3

---

## 👤 Credits

* **Me**

Happy Reversing 😉
