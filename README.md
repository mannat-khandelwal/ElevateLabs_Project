# ElevateLabs_Project

🔐 Password Strength Analyzer & Custom Wordlist Generator

📌 Introduction

- This is a Python-based CLI tool that:

- Analyzes the strength of a given password.

- Generates a custom wordlist using personal inputs such as name, pet name, and dates.

- Applies leetspeak substitutions (e.g., a → 4, e → 3) and year variations (±10 years).

- Saves the generated wordlist in a .txt file.

- The tool is designed for educational purposes in cybersecurity to demonstrate how weak or predictable passwords can be exploited.

⚙️ Features

✅ Simple password strength checker (Weak / Medium / Strong).

✅ Personalized wordlist generator with user inputs.

✅ Automatic year variations for common patterns.

✅ Exports results to a .txt file.

✅ Lightweight – uses only Python’s standard libraries.

🛠️ Requirements

Python 3.x

No external dependencies required

🚀 Usage

1. Run the Tool
python tool.py --password MyPass123! --name Alex --pet Simba --date 2001 --output mylist.txt

2 . Arguments
Argument	Description	Example
--password	Password to check strength	MyPass123!
--name	Name input (optional)	Alex
--pet	Pet name input (optional)	Simba
--date	Date input (optional)	2001
--output	Output file for wordlist (default: simple_wordlist.txt)	mylist.txt

📊 Example

Command:
python tool.py --password HelloWorld123! --name XYZ --pet Simba --date 2001 --output mylist.txt

Output:
Password Strength: Strong
Wordlist saved to mylist.txt with 253 entries.

Sample Entries in mylist.txt:
xyz2001
2001xyz
s1mba
simba2023
h3llo

📂 File Structure
 ┣ 📜 tool.py            # Main script
 ┣ 📜 README.md          # Documentation
 ┗ 📜 simple_wordlist.txt # Generated wordlist (after running)

⚠️ Disclaimer

This project is for educational and research purposes only. Do not use it for unauthorized access or illegal activities. Always follow ethical hacking practices.
