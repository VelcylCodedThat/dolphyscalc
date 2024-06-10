import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, sympify, diff, integrate, solve, limit, series

def calculate_function_properties(func, x):
    # Calculate domain, range, x-intercepts, y-intercepts, derivative, integral, asymptotes, intervals of increase and decrease, critical points, extrema points, intervals of concavity, inflection points, limit, Taylor polynomial, and graph of the single-variable function
    x_symbol = symbols('x')
    func_symbol = sympify(func)
    
    # Domain
    domain = solve(func_symbol, x_symbol)
    
    # Range
    range_ = [func_symbol.subs(x_symbol, i) for i in domain]
    
    # X-intercepts
    x_intercepts = [i for i in domain if func_symbol.subs(x_symbol, i) == 0]
    
    # Y-intercepts
    y_intercepts = [func_symbol.subs(x_symbol, 0)]
    
    # Derivative
    derivative = diff(func_symbol, x_symbol)
    
    # Integral
    integral = integrate(func_symbol, x_symbol)
    
    # Asymptotes
    asymptotes = [limit(func_symbol, x_symbol, i) for i in [-float('inf'), float('inf')]]
    
    # Intervals of increase and decrease
    intervals_increase = solve(diff(func_symbol, x_symbol) > 0, x_symbol)
    intervals_decrease = solve(diff(func_symbol, x_symbol) < 0, x_symbol)
    
    # Critical points
    critical_points = solve(diff(func_symbol, x_symbol), x_symbol)
    
    # Extrema points
    extrema_points = solve(diff(diff(func_symbol, x_symbol), x_symbol), x_symbol)
    
    # Intervals of concavity
    intervals_concavity = solve(diff(diff(func_symbol, x_symbol), x_symbol) > 0, x_symbol)
    
    # Inflection points
    inflection_points = solve(diff(diff(func_symbol, x_symbol), x_symbol), x_symbol)
    
    # Limit
    limit_ = limit(func_symbol, x_symbol, float('inf'))
    
    # Taylor polynomial
    taylor_polynomial = series(func_symbol, x_symbol, 0, 10)
    
    # Graph
    try:
        plt.clf()  # Clear the canvas
        x_values = np.linspace(-10, 10, 400)
        y_values = [float(func_symbol.subs(x_symbol, i)) for i in x_values]
        plt.plot(x_values, y_values)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Graph of the function')
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Error graphing: {str(e)}")
    
    return {
        'domain': domain,
        'range': range_,
        'x_intercepts': x_intercepts,
        'y_intercepts': y_intercepts,
        'derivative': derivative,
        'integral': integral,
        'asymptotes': asymptotes,
        'intervals_increase': intervals_increase,
        'intervals_decrease': intervals_decrease,
        'critical_points': critical_points,
        'extrema_points': extrema_points,
        'intervals_concavity': intervals_concavity,
        'inflection_points': inflection_points,
        'limit': limit_,
        'taylor_polynomial': taylor_polynomial
    }

def normal_math():
    print("Normal Math Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Exponentiation")
    print("7. Logarithm")
    print("8. Trigonometry")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print(f"The result is: {result}")
    elif choice == 2:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 - num2
        print(f"The result is: {result}")
    elif choice == 3:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 * num2
        print(f"The result is: {result}")
    elif choice == 4:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num2 != 0:
            result =num1 / num2
            print(f"The result is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    elif choice == 5:
        num = float(input("Enter the number: "))
        if num >= 0:
            result = num ** 0.5
            print(f"The result is: {result}")
        else:
            print("Error: Cannot calculate the square root of a negative number.")
    elif choice == 6:
        num1 = float(input("Enter the base: "))
        num2 = float(input("Enter the exponent: "))
        if num1 > 0 and num2 >= 0:
            result = num1 ** num2
            print(f"The result is: {result}")
        else:
            print("Error: The base must be positive and the exponent must be non-negative.")
    elif choice == 7:
        num = float(input("Enter the number: "))
        if num > 0:
            base = float(input("Enter the base: "))
            if base > 0 and base != 1:
                result = np.log(num) / np.log(base)
                print(f"The result is: {result}")
            else:
                print("Error: The base must be positive and not equal to 1.")
        else:
            print("Error: The number must be positive.")
    elif choice == 8:
        print("Trigonometry:")
        print("1. Sine")
        print("2. Cosine")
        print("3. Tangent")
        
        trig_choice = int(input("Enter your choice: "))
        
        if trig_choice == 1:
            angle = float(input("Enter the angle in degrees: "))
            result = np.sin(np.radians(angle))
            print(f"The result is: {result}")
        elif trig_choice == 2:
            angle = float(input("Enter the angle in degrees: "))
            result = np.cos(np.radians(angle))
            print(f"The result is: {result}")
        elif trig_choice == 3:
            angle = float(input("Enter the angle in degrees: "))
            result = np.tan(np.radians(angle))
            print(f"The result is: {result}")
        else:
            print("Invalid choice. Please try again.")
    else:
        print("Invalid choice. Please try again.")
def main():
    while True:
        print("Delphys")
        print("Made By VelCT")
        print("Calculator Menu:")
        print("1. Function Calculator")
        print("2. Normal Math Operations")
        print("3. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            func = input("Enter the function (in the format 'x**2 + 3*x + 2'): ")
            x = symbols('x')
            properties = calculate_function_properties(func, x)
            print("Properties of the function:")
            for key, value in properties.items():
                print(f"{key.capitalize()}: {value}")
        elif choice == 2:
            normal_math()
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()