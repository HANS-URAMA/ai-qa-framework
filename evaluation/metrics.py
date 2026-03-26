def accuracy(predictions, expected):
    correct = sum([1 for p, e in zip(predictions, expected) if p == e])
    return correct / len(predictions)

def consistency(predictions):
    return len(set(predictions)) / len(predictions)

def hallucination_rate(predictions):
    hallucinations = [p for p in predictions if "not sure" in p.lower()]
    return len(hallucinations) / len(predictions)