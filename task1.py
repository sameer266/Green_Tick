import re

suspecious_pattern = ["failed login","unauthorized access","malicious activity detected"]

def get_time(line):
    regex = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", line)
    if regex:
        return regex.group(0)
    return None

def check_log(log_file):
    try:
        with open(log_file,'r') as file:
            for line in file:
                for word in suspecious_pattern:
                    if word in line.lower():
                        time = get_time(line)
                        if time:
                            print(f"Alert: {word} attempt detected at {time}")
                        else:
                            print(f"Alert: {word} attempt detected ")
    except Exception as e:
        print(f"Error: {str(e)}")

log_file = input("Enter the file path: ")
check_log(log_file)
