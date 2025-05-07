![Hacker GIF](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNnExZ2F6ejAxbW84Z3hyem9ua21lcjI5ajhmc2trOWJyZWVmZHB4dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YQitE4YNQNahy/giphy.gif)

# HellMart

## Description
**HellMart** is a fast, multi-threaded directory fuzzing tool designed for ethical hackers, penetration testers, and security researchers. The tool helps uncover hidden directories and files on a target web server by fuzzing a given URL with a wordlist.

With its efficient multi-threaded architecture, HellMart is optimized for speed, making it an ideal solution for web application reconnaissance. The tool supports customizable wordlists and provides clear results, including found directories, forbidden access directories, and those that couldn't be found. Results are saved for later analysis in a `results.txt` file.

**HellMart** is designed for ethical use only—ensure that you have permission to test the target web server before using this tool.

## Features
- **Multi-threaded**: Speed up directory fuzzing with multi-threading.
- **Customizable wordlists**: Use your own wordlist or the default one.
- **Clear output**: The results clearly indicate found, forbidden, and not found directories.
- **Graceful exit**: Supports clean interruption using Ctrl+C and waits for threads to complete.
- **Result Logging**: All found results are logged into a `results.txt` file.

## Requirements
- Python 3.x
- `requests` library

You can install this tool by this instructions:
```bash
pip install requests
git clone https://github.com/MASTERMONTYOFFICIAL/hellmart.git
python3 hellmart.py
```

## 🙌 Stay Connected

Thank you for checking out **HellMart**! Your support means a lot. If this tool helped you, feel free to give the repo a ⭐ star, share it with others, and subscribe to my channel for more hacking tools and tutorials.

## **Support My Work**
If you find **HellMart** helpful, please consider subscribing to my YouTube channel for more tutorials, ethical hacking tools, and security tips!
[![Subscribe to my YouTube Channel: @Unr3veledTr4netra](https://img.shields.io/badge/Subscribe-YouTube-red)](https://www.youtube.com/@Unr3veledTr4netra)

> ⚠️ This tool is made for educational purposes and legal penetration testing only. Use responsibly.





