import unittest
from testFile.py import function1, function2


class TestFileName(unittest.TestCase):
    def test_function1(self):
        self.assertEqual(function1(1), 0)

    def test_function2(self):
        self.assertEqual(function2(2,1), 3)
        self.assertEqual(function2(2.1, 1.2), 3.3)

if __name__ == '__main__':
    unittest.main()

name: Tests
on: push

jobs:
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Setup python
        uses: actions/setup-python@v2
        with:
          python-version: 3.6

      - name: Install tools
        run: |
          python -m pip install --upgrade pip pytest
          pip install coverage                          

      - name: Test with unittest
        run: python3 -m unittest test.py

      - name: Check code coverage                       
        run: |
          python3 -m coverage run -m unittest test.py
          python3 -m coverage report
          python3 -m coverage html

      - name: Archive code coverage HTML report
        uses: actions/upload-artifact@v2
        with:
           name: code-coverage-report
           path: htmlcov
