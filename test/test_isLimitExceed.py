import sys
sys.path.append("")
from app.routes.events import isLimitExceed
import pytest

def test_high_volume_events():
    events = [i for i in range(200000)]  # 200 events within 200 seconds
    assert isLimitExceed(events) == False

def test_exceeds_limit():
    events = [i % 5 for i in range(101)]  # 101 events within 60 seconds
    assert isLimitExceed(events) == True

def test_does_not_exceed_limit():
    events = [i for i in range(100)]  # 100 events within 100 seconds
    assert isLimitExceed(events) == False

def test_non_sorted_input():
    events = [10, 5, 1, 2, 5, 8, 3, 4] * 5  # 120 events but not exceeding limit in any 60s window
    assert isLimitExceed(events) == False

def test_invalid_input():
    events = ["a", "b", "c"]  # Invalid input
    with pytest.raises(ValueError):
        isLimitExceed(events)

if __name__ == "__main__":
    pass