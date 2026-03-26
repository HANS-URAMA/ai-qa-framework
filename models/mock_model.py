import random

def predict(input_text):
    responses = [
        "Yes, this is correct.",
        "No, this is incorrect.",
        "I'm not sure.",
        "The answer is partially correct."
    ]
    return random.choice(responses)