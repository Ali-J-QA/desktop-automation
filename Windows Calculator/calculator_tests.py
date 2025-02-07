# test_calculator.py
from calculatorApp import WindowsCalculator
from logger import log_result

def test_addition():
    calc = WindowsCalculator()
    calc.open_calc()
    calc.perform_calculation("2+2")
    result = calc.get_result_from_clipboard()
    expected_result = "4"  # Expected result of the calculation
    log_result(expected_result, result)
    calc.close_calc()

def test_multiplication():
    calc = WindowsCalculator()
    calc.open_calc()
    calc.perform_calculation("5*5")
    result = calc.get_result_from_clipboard()
    expected_result = "25"  # Expected result of the calculation
    log_result(expected_result, result)
    calc.close_calc()

#given the outputs from calc are reliable
#this test forces a failure with an incorrect expected result
def test_multiplication_forced_failure():
    calc = WindowsCalculator()
    calc.open_calc()
    calc.perform_calculation("5*5")
    result = calc.get_result_from_clipboard()
    expected_result = "26"  # Expected result of the calculation
    log_result(expected_result, result)
    calc.close_calc()

if __name__ == "__main__":
    test_addition()
    test_multiplication_forced_failure()
    test_multiplication()
    