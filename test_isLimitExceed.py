from main import isLimitExceed
import unittest

class TestIsLimitExceed(unittest.TestCase):
    def test_exceeds_limit(self):
        events = [i % 5 for i in range(101)]  # 101 events within 60 seconds
        self.assertTrue(isLimitExceed(events))

    def test_does_not_exceed_limit(self):
        events = [i for i in range(100)]  # 100 events within 100 seconds
        self.assertFalse(isLimitExceed(events))

    def test_non_sorted_input(self):
        events = [10, 5, 1, 2, 5, 8, 3, 4] * 5  # 120 events but not exceeding limit in any 60s window
        self.assertFalse(isLimitExceed(events))

    def test_invalid_input(self):
        events = ["a", "b", "c"]  # Invalid input
        with self.assertRaises(ValueError):
            isLimitExceed(events)
            
if __name__ == "__main__":
    unittest.main()