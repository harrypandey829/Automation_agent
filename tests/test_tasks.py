import tempfile
import os
from app.tasks import count_wednesdays

def test_count_wednesdays():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file.write("2024-01-03\n2024-02-07\n2024-03-13\n")  # Sample Wednesdays
        temp_file.flush()  # Ensure data is written to disk

    result = count_wednesdays(temp_file.name)  # Call the function with temp file
    assert result == 3  # Expecting 3 Wednesdays

    # Check if the output file was created
    output_file = "./output/dates-wednesdays.txt"
    assert os.path.exists(output_file)

    # Read and validate the output file
    with open(output_file, 'r') as f:
        content = f.read()
        assert "Total Wednesdays: 3" in content
