import os
import subprocess
from .utils import query_llm

def execute_task(task_description):
    if "count Wednesdays" in task_description:
        return count_wednesdays("/data/dates.txt")
    elif "extract sender" in task_description:
        return extract_email_sender("/data/email.txt")
    else:
        raise ValueError("Unknown task description")

def count_wednesdays(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError("File not found")
    with open(file_path, 'r') as f:
        lines = f.readlines()
    count = sum(1 for line in lines if "Wednesday" in line)
    with open("/data/dates-wednesdays.txt", 'w') as f:
        f.write(str(count))
    return count

def extract_email_sender(file_path):
    content = open(file_path).read()
    response = query_llm(f"Extract sender email from this text: {content}")
    with open("/data/email-sender.txt", 'w') as f:
        f.write(response)
    return response