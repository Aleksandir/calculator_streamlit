# Streamlit Calculator App

This is a simple calculator app built with Python and Streamlit. It supports basic arithmetic operations like addition, subtraction, multiplication, division, and exponentiation.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, division
- Exponentiation (squared operation)
- Percentage calculation
- Clear calculation
- Error handling for invalid calculations

## How to Run

You can access the live app at [https://calcapp.streamlit.app/](https://calcapp.streamlit.app/)

## Code Structure

The main logic of the calculator is handled by the `key_press` function, which updates the calculation based on the key that was pressed. The `evaluate_calculation` function is used to evaluate the calculation string and return the result.

The layout for the calculator display and buttons is defined in the main part of the script.

## Future Improvements

- Support for more advanced mathematical operations
- Improved error handling and user feedback
- add keyboard input support (may require a different framework eg. flask)
