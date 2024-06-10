Welcome to Dolphys!

This is a Python script that provides a simple calculator with two main features:

Function Calculator: This feature allows the user to input a single-variable function, and the script will calculate and display various properties of the function, including:
Domain
Range
X-intercepts
Y-intercepts
Derivative
Integral
Asymptotes
Intervals of increase and decrease
Critical points
Extrema points
Intervals of concavity
Inflection points
Limit
Taylor polynomial
Graph of the function
Normal Math Operations: This feature allows the user to perform basic arithmetic operations, including:
Addition
Subtraction
Multiplication
Division
Square Root
Here's a breakdown of the code:

Importing libraries:

The script imports three libraries:

matplotlib.pyplot for plotting the graph of the function
numpy for numerical computations
sympy for symbolic mathematics (e.g., differentiating and integrating functions)
Function Calculator:

The calculate_function_properties function takes a string input func representing the function and a symbol x representing the variable. It calculates the various properties of the function using SymPy and returns a dictionary with the results.

The function uses a try-except block to evaluate the function at different points to determine the domain. It then calculates the range, x-intercepts, y-intercepts, derivative, integral, and other properties using SymPy functions.

Normal Math Operations:

The normal_math function provides a simple menu for the user to choose from basic arithmetic operations. It takes input from the user and performs the selected operation.

Main function:

The main function is the entry point of the script. It displays a menu with two options: Function Calculator and Normal Math Operations. Based on the user's choice, it calls either the calculate_function_properties function or the normal_math function.

Execution:

The script is executed when the if __name__ == "__main__": block is reached. This block ensures that the main function is called only when the script is run directly (i.e., not when it's imported as a module by another script).

