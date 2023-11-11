import re

import streamlit as st

# TODO calculate when enter is pressed
# TODO add keyboard support
# TODO add history
# TODO add unit tests


def evaluate_calculation(calculation):
    """
    Evaluates a mathematical calculation string and returns the result.

    Args:
        calculation (str): A string representing a mathematical calculation.

    Returns:
        str: The result of the calculation as a string, or "Error" if the calculation is invalid.
    """
    try:
        # Add * between number and (
        calculation = re.sub(r"(\d)\(", r"\1*(", calculation)
        # Add * between ) and number
        calculation = re.sub(r"\)(\d)", r")*\1", calculation)
        calculation = str(eval(calculation))
        if calculation.endswith(".0"):
            calculation = calculation[:-2]
        return calculation
    except Exception as e:
        st.write(f"Error: {str(e)}")


def key_press(key):
    if key.isdigit() or key in ["+", "-", "*", "/", "(", ")", "."]:
        st.session_state["calculation"] += key
    elif key == "x":
        st.session_state["calculation"] += "*"
    elif key == "^":
        st.session_state["calculation"] += "**"
    elif key == "=":
        try:
            st.session_state["calculation"] = evaluate_calculation(
                st.session_state["calculation"]
            )
        except Exception as e:
            st.write(f"Error: {str(e)}")
    elif key == "c":
        st.session_state["calculation"] = ""  # Clear the calculation
    else:
        pass  # Ignore other characters

    calc_display.text_input("Calculation", st.session_state["calculation"])


# layout for calculator display
st.title("Calculator")
calc_display = st.empty()

if "calculation" not in st.session_state:
    st.session_state["calculation"] = ""

calc_display.text_input(st.session_state["calculation"])

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
    if st.button("&#42;"):  # HTML entity for *
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
        key_press("**")
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
