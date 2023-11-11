import streamlit as st

# Create a 3x3 grid
grid = [[None for _ in range(3)] for _ in range(3)]

# Loop through the grid
for i in range(3):
    cols = st.beta_columns(3)
    for j in range(3):
        # Create a button in each cell
        grid[i][j] = cols[j].button(f"Button {i*3 + j + 1}")
