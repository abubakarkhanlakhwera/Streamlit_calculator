import streamlit as st

# Available operators
operators = ['+', '-', '*', '/']

# User input for numbers and operator
st.title("Simple Calculator")

x = st.number_input('Enter first number:', format="%f")
y = st.number_input('Enter second number:', format="%f")
select = st.selectbox('Select operator:', operators)

# Perform the calculation
if select in operators:
    if select == '+':
        st.write(f"Result: {x + y}")
    elif select == '-':
        st.write(f"Result: {x - y}")
    elif select == '*':
        st.write(f"Result: {x * y}")
    elif select == '/':
        if y != 0:
            st.write(f"Result: {x / y}")
        else:
            st.write("Error: Division by zero is not allowed.")
else:
    st.write("Invalid operator")
