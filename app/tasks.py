import os
import subprocess
from .utils import query_llm

# Ensure the output directory exists
OUTPUT_DIR = "./output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def execute_task(task_description):
    if "count Wednesdays" in task_description:
        return count_wednesdays("./output/dates.txt")  # Update path
    elif "extract sender" in task_description:
        return extract_email_sender("./output/email.txt")  # Update path
    else:
        raise ValueError("Unknown task description")

def count_wednesdays(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError("File not found")
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    count = sum(1 for line in lines if "Wednesday" in line)

    # Write output to a writable directory
    output_file = os.path.join(OUTPUT_DIR, "dates-wednesdays.txt")
    with open(output_file, 'w') as f:
        f.write(str(count))
    
    return count

def extract_email_sender(file_path):
    content = open(file_path).read()
    response = query_llm(f"Extract sender email from this text: {content}")

    # Write output to a writable directory
    output_file = os.path.join(OUTPUT_DIR, "email-sender.txt")
    with open(output_file, 'w') as f:
        f.write(response)

    return response
