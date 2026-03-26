def generate_report(results):
    print("=== AI QA Report ===")
    for key, value in results.items():
        print(f"{key}: {value:.2f}")