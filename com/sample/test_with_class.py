import pytest

# Test Class with name Demo
## we can group tests in class and run them class by class too.
import pytest

class TestDemoClass:
    val = 0
    def test_one(self):
        self.val += 1
        assert self.val == 1

    # this will fail since class variables are shared across functions
    def test_two(self):
        print(self.val)
        assert self.val == 0
