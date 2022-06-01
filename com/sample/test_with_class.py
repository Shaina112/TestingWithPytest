import pytest

# Test Class with name Demo
## we can group tests in class and run them class by class too.
import pytest

class TestDemoClass:
    val = 0
    def test_one(self):
        self.val += 1
        assert self.val == 1

    # this will not fail since each test has it;s own instance of the class
    def test_two(self):
        print(self.val)
        assert self.val == 0
