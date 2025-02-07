# run_tests.py
import os

# Read the test functions from the configuration file
def load_tests_from_config(config_file):
    with open(config_file, "r") as f:
        tests = [line.strip() for line in f.readlines() if line.strip()]
    return tests

# Run the tests dynamically
def run_tests():
    # Load test names from the configuration file
    config_file = "test_config.txt"
    test_names = load_tests_from_config(config_file)
    
    # Import the calculator_tests module
    import calculator_tests
    
    # Dynamically run the tests
    for test_name in test_names:
        test_func = getattr(calculator_tests, test_name, None)
        if callable(test_func):
            print(f"Running {test_name}...")
            test_func()  # Call the test function
        else:
            print(f"Test function {test_name} not found!")

if __name__ == "__main__":
    run_tests()
