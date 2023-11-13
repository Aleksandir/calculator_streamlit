# Description: Unit tests for main.py

from main import evaluate_calculation


def test_evaluate_calculation():
    assert evaluate_calculation("") == ""
    assert evaluate_calculation("1+2") == "3"
    assert evaluate_calculation("2*3") == "6"
    assert evaluate_calculation("4/2") == "2"
    assert evaluate_calculation("5-3") == "2"
    assert evaluate_calculation("2*(3+4)") == "14"
    assert evaluate_calculation("(3+4)*2") == "14"
    assert evaluate_calculation("1/0") == "Error"
    assert evaluate_calculation("1 + 2 * 3") == "7"
    assert evaluate_calculation("(1 + 2) * 3") == "9"
    assert evaluate_calculation("1 + (2 * 3)") == "7"
    assert evaluate_calculation("1 + (2 * 3))") == "Error"
    assert evaluate_calculation("1 + (2 * 3)") == "7"
    assert evaluate_calculation("1 + (2 * 3))") == "Error"


if __name__ == "__main__":
    test_evaluate_calculation()
