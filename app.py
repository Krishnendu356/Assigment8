import streamlit as st

def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

st.title("Find the largest among three numbers")
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
num3 = st.number_input("Enter the third number:")
if st.button("Find largest"):
    result = find_largest(num1, num2, num3)
    st.write("The largest number is:", result)
