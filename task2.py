from bs4 import BeautifulSoup
import requests
missing_headers = ["X-Content-Type-Options", "Strict-Transport-Security"]
vuln_software = ["Apache/2.2.0","nginx/1.18.0","Mysql/5.2.0"]

def check_headers(url):
    response= requests.get(url)
    headers = []
    for header in missing_headers:
        if header not in response.headers:
            headers.append(header)
    return headers

def checkOutdated_software(url):
    response = requests.get(url)
    outdated_software = []
    for i in vuln_software:
        if i.lower() in response.text.lower():
            outdated_software.append(i)
    return outdated_software



def check_forms(url):
    response = requests.get(url)
    soup= BeautifulSoup(response.text, 'html.parser')
    forms_data= soup.find_all('form')
    insecure_form= []
    for form in forms_data:
        action= form.get('action')
        method= form.get('method')
        if not action or method != "POST":
            insecure_form.append(action)
    return insecure_form


def scan_web(url):
    try:
        print(f"Scanning Website {url} .....")
        missing_header= check_headers(url)
        outdated_software= checkOutdated_software(url)
        insecure_form = check_forms(url)
        print(f"Vulnerability Scan Report For {url}")
        if missing_header:
            for i in missing_header:
                print(f"Missing Security Headers: {i}")
        if outdated_software:
            for i in outdated_software:
                print(f"Outdated Software Version Detected: {i}")
        if insecure_form:
            for i in insecure_form:
                print(f"Form without proper Method Attribute: {i}") 
        
        if not missing_header and not outdated_software and not insecure_form:
            print(f"No vulnerabilities found")
    except Exception as e:
        print(f"Error in  {str(e)}")

user_url= input("Enter a URL to scan: ")
scan_web(user_url)
