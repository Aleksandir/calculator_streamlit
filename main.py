import re

import streamlit as st

# TODO calculate when enter is pressed
# TODO add keyboard support
# TODO add history
# TODO add unit tests

# Create a placeholder for the text input
calc_display = st.empty()


def update_display(display_text):
    """
    Updates the calculator display.

    Args:
        display_text (str): The text to display.

    Returns:
        None
    """
    if "calc_display_exists" not in st.session_state:
        st.session_state["calc_display_exists"] = False

    if not st.session_state["calc_display_exists"]:
        st.session_state["calculation"] = calc_display.text_input(
            "Calculation", st.session_state["calculation"]
        )
        st.session_state["calc_display_exists"] = True

    calc_display.text_input("Calculation", display_text)


def evaluate_calculation(calculation):
    """
    Evaluates a mathematical calculation string and returns the result.

    Args:
        calculation (str): A string representing a mathematical calculation.

    Returns:
        str: The result of the calculation as a string, or "Error" if the calculation is invalid.
    """
    if calculation == "":
        return ""
    else:
        try:
            # Add * between number and (
            calculation = re.sub(r"(\d)\(", r"\1*(", calculation)
            # Add * between ) and number
            calculation = re.sub(r"\)(\d)", r")*\1", calculation)
            calculation = str(eval(calculation))
            if calculation.endswith(".0"):
                calculation = calculation[:-2]
            return calculation
        except Exception:
            return "Error"


def calculate(calculation):
    try:
        st.session_state["calculation"] = evaluate_calculation(
            st.session_state["calculation"]
        )
    except Exception as e:
        st.write(f"Error: {str(e)}")


def key_press(key):
    """
    Handles key press events for the calculator.

    Args:
        key (str): The key that was pressed.

    Returns:
        None
    """
    # if calculation is currently "error" and a key is pressed, clear the error
    if st.session_state["calculation"] == "Error":
        st.session_state["calculation"] = ""

    match key:
        case _ if key.isdigit() or key in ["+", "-", "*", "/", "(", ")", "."]:
            st.session_state["calculation"] += key
        case "x":
            st.session_state["calculation"] += "*"
        case "**2":
            # if calculation is empty, pressing x² does nothing
            if st.session_state["calculation"] == "":
                update_display("Error")
                return
            # if calculation ends with a number, add **2 and calculate
            else:
                st.session_state["calculation"] += "**2"
                calculate(st.session_state["calculation"])
        case "=":
            calculate(st.session_state["calculation"])
        case "c":
            st.session_state["calculation"] = ""  # Clear the calculation
        case "%":
            st.session_state["calculation"] += "/100"
        case _:
            pass

    update_display(st.session_state["calculation"])


# layout for calculator display


def main():
    calc_display = st.empty()

    if "calculation" not in st.session_state:
        st.session_state["calculation"] = ""

    if "calc_display_exists" not in st.session_state:
        st.session_state["calc_display_exists"] = False

    if not st.session_state["calc_display_exists"]:
        user_input = st.session_state["calculation"] = calc_display.text_input(
            "Calculation", st.session_state["calculation"]
        )
        st.session_state["calc_display_exists"] = True

    # Create layout for calculator buttons
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("1"):
            key_press("1")
    with col2:
        if st.button("2"):
            key_press("2")
    with col3:
        if st.button("3"):
            key_press("3")
    with col4:
        if st.button("&#43;"):  # HTML entity for +
            key_press("+")
    with col5:
        if st.button("&#45;"):  # HTML entity for -
            key_press("-")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("4"):
            key_press("4")
    with col2:
        if st.button("5"):
            key_press("5")
    with col3:
        if st.button("6"):
            key_press("6")
    with col4:
        if st.button("x"):  # HTML entity for *
            key_press("*")
    with col5:
        if st.button("/"):
            key_press("/")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("7"):
            key_press("7")
    with col2:
        if st.button("8"):
            key_press("8")
    with col3:
        if st.button("9"):
            key_press("9")
    with col4:
        if st.button("x²"):
            key_press("**2")
    with col5:
        if st.button("%"):
            key_press("%")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("("):
            key_press("(")
    with col2:
        if st.button("0"):
            key_press("0")
    with col3:
        if st.button(")"):
            key_press(")")
    with col4:
        if st.button("AC"):
            key_press("c")
    with col5:
        if st.button("="):
            key_press("=")


if __name__ == "__main__":
    main()
