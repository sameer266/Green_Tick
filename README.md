# Log & Web Security Scanner

## Overview
This project consists of two Python scripts that help in security analysis:
1. **task1.py** - Scans log files for suspicious activity patterns.
2. **task2.py** - Scans websites for security vulnerabilities, including missing security headers, outdated software, and insecure forms.

## Requirements
Ensure you have Python installed along with the required libraries:
```bash
pip install beautifulsoup4 requests
```

## Usage
### Task 1: Log File Security Scanner
This script scans a given log file for suspicious activity patterns such as unauthorized access or failed login attempts.
#### Running the script:
```bash
python task1.py
```
Then enter the log file path when prompted.

### Task 2: Website Security Scanner
This script scans a given URL for security vulnerabilities.
#### Running the script:
```bash
python task2.py
```
Then enter the URL when prompted.

## Features
### Task 1 (Log Scanner):
- Detects suspicious patterns like:
  - "failed login"
  - "unauthorized access"
  - "malicious activity detected"
- Extracts and displays timestamps of suspicious activity.

### Task 2 (Web Security Scanner):
- Checks for **missing security headers** (e.g., `X-Content-Type-Options`, `Strict-Transport-Security`).
- Detects **outdated software versions** known to have vulnerabilities.
- Identifies **insecure forms** missing `POST` method or action attributes.

## Example Output
### Task 1:
```
Enter the file path: logs.txt
Alert: unauthorized access attempt detected at 2025-03-01 13:15:23
```
### Task 2:
```
Enter a URL to scan: http://example.com
Scanning Website http://example.com .....
Vulnerability Scan Report For http://example.com
Missing Security Headers: X-Content-Type-Options
Outdated Software Version Detected: Apache/2.2.0
Form without proper Method Attribute: /login
```

## Disclaimer
This tool is intended for educational purposes and security auditing of your own systems. Do not use it to scan websites without permission.

