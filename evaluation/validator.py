from models.mock_model import predict
from evaluation.metrics import accuracy, consistency, hallucination_rate

def run_validation(test_cases):
    predictions = []
    expected = []

    for case in test_cases:
        pred = predict(case["input"])
        predictions.append(pred)
        expected.append(case["expected"])

    results = {
        "accuracy": accuracy(predictions, expected),
        "consistency": consistency(predictions),
        "hallucination_rate": hallucination_rate(predictions)
    }

    return results