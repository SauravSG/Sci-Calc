import streamlit as st
import webbrowser
import math 
# import numpy as np
st.title("Scientific Calculator")

first_number = st.text_input("Enter number", "0")

operation = st.selectbox("operation: ", ["square", "square root", "cube", "factorial","log", "sin", "cos", "tan"])

if st.button("Perform Operation"):
	
	if operation=="square":
		result = int (first_number) * int(first_number)
		st.success(f"Your result is {result}")
	if operation=="cube":
		result = int (first_number) * int(first_number) * int(first_number)
		st.success(f"Your result is {result}")
	if operation=="factorial":
		n = int(first_number)
		result = math.factorial(n)
		st.success(f"Your result is {result}")
	if operation=="square root":
		n = int(first_number)
		result = math.sqrt(n)
		st.success(f"Your result is {result}")
	if operation=="log":
		n = int(first_number)
		result = math.log(n)
		st.success(f"Your result is {result}")
	if operation=="cos":
		n = int(first_number)
		result = math.cos(n)
		st.success(f"Your result is {result}")
	if operation=="sin":
		n = int(first_number)
		result = math.sin(n)
		st.success(f"Your result is {result}")
	if operation=="tan":
		n = int(first_number)
		result = math.tan(n)
		st.success(f"Your result is {result}")

if st.button("Switch To Standard Operation"):
	webbrowser.open("https://share.streamlit.io/sauravsg/std-calc/main/calculator.py")