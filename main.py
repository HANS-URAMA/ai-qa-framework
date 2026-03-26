from tests.test_runner import run_tests
from reports.report_generator import generate_report

if __name__ == "__main__":
    results = run_tests()
    generate_report(results)