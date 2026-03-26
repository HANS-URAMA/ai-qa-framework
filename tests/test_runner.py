import json
from evaluation.validator import run_validation

def run_tests():
    with open("data/test_cases.json") as f:
        test_cases = json.load(f)

    results = run_validation(test_cases)
    return results