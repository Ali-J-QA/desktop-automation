import os

def load_tests_from_config(config_file):
    with open(config_file, "r") as f:
        tests = [line.strip() for line in f.readlines() if line.strip()]
    return tests

def run_tests():
    config_file = "test_config.txt"
    test_names = load_tests_from_config(config_file)
    
    import calculator_tests
    
    for test_name in test_names:
        test_func = getattr(calculator_tests, test_name, None)
        if callable(test_func):
            print(f"Running {test_name}...")
            test_func()  
        else:
            print(f"Test function {test_name} not found!")

if __name__ == "__main__":
    run_tests()
