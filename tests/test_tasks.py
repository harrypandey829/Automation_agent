import pytest
from app.tasks import count_wednesdays

def test_count_wednesdays():
    with open("/data/dates.txt", 'w') as f:
        f.write("Monday\nWednesday\nWednesday\nSunday\n")
    assert count_wednesdays("/data/dates.txt") == 2