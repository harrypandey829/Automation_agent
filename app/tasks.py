import os
import datetime
from .utils import query_llm

# Ensure the output directory exists
OUTPUT_DIR = "./output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def count_wednesdays(file_path):
    """Count how many dates in the file fall on a Wednesday."""
    if not os.path.exists(file_path):
        raise FileNotFoundError("File not found")
    
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Convert dates to weekdays and count Wednesdays
    count = 0
    for line in lines:
        date_str = line.strip()
        try:
            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            if date_obj.strftime("%A") == "Wednesday":
                count += 1
        except ValueError:
            continue  # Ignore invalid dates

    # Save the count result
    output_file = os.path.join(OUTPUT_DIR, "dates-wednesdays.txt")
    with open(output_file, 'w') as f:
        f.write(str(count))

    return count
