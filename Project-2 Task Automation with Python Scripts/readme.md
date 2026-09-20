# Task Automation with Python Scripts — Email Extractor

A simple Python script that automates a repetitive task: extracting all email addresses from a `.txt` file and saving them into a separate output file. Built as **Project 2** for the CodeAlpha Python Internship.

## 📌 Description

This program reads the contents of a user-specified text file, uses a regular expression (regex) pattern to find all email addresses within it, and writes the extracted emails into a new file — one email per line. If no emails are found, the program notifies the user and exits.

## ✨ Features

- Takes any `.txt` file name as input
- Uses regex (`re` module) to accurately detect email addresses
- Handles the case where no emails are found in the file
- Saves all extracted emails to `output_file.txt`, one per line
- Displays a confirmation message showing how many emails were found

## 🛠️ Concepts Used

- `re` module (regular expressions / pattern matching)
- File handling (`open()`, `.read()`, `.write()`, `with` statement)
- String pattern matching (`re.findall()`)
- Basic input/output and conditional checks (`exit()`)

## ▶️ How to Run

```bash
python3 Task_Automation_with_Python_ Scripts.py
```

Follow the prompt:
1. Enter the name of the `.txt` file to scan (e.g. `sample.txt`)
2. The script scans the file for email addresses
3. If emails are found, they are saved to `output_file.txt`
4. A message shows how many emails were extracted

## 📄 Sample Input / Output

**Input (`sample.txt`):** A text file containing a mix of regular text and email addresses (e.g. contact info, support emails).

**Output (`output_file.txt`):**
```
info@example.com
support@test.org
sales.team@company.co
ali.khan@gmail.com
tech-support123@service.net
newsletter_updates@mailinglist.io
```

## 👤 Author

CodeAlpha Python Internship — Project 2