import math
import random
import os

# Set the terminal background to dark gray (ANSI escape sequence)
os.system('')  # Enable ANSI escape codes on Windows
print("\033[40m", end="")  # Set background to dark gray

# Title of the game
print("\033[1;37m\n===== Guess the Formula =====\n\033[0m")  # Bold white title

# List of functions and their descriptions
functions = [
    {"formula": "A = a^2", "use": "Calculating the area of a square", "type": "Geometry"},
    {"formula": "A = lw", "use": "Calculating the area of a rectangle", "type": "Geometry"},
    {"formula": "y = mx + b", "use": "Slope-intercept form of a line", "type": "Algebra"},
    {"formula": "a^2 + b^2 = c^2", "use": "Pythagorean theorem", "type": "Geometry"},
    {"formula": "A = 1/2bh", "use": "Calculating the area of a triangle", "type": "Geometry"},
    {"formula": "sin^2(\u03B8) + cos^2(\u03B8) = 1", "use": "Trigonometric identity", "type": "Trigonometry"},
    {"formula": "a^2 - b^2 = (a - b)(a + b)", "use": "Difference of squares", "type": "Algebra"},
    {"formula": "m = (y2 - y1) / (x2 - x1)", "use": "Slope of a line", "type": "Algebra"},
    {"formula": "a/sin(A) = b/sin(B) = c/sin(C)", "use": "Law of sines", "type": "Trigonometry"},
    {"formula": "sum = (n - 2) x 180°", "use": "Sum of interior angles of a polygon", "type": "Geometry"},
    {"formula": "e^{ix} = cos(x) + i*sin(x)", "use": "Euler's formula", "type": "Complex Analysis"},
    {"formula": "(1 + x)^n \u2265 1 + nx", "use": "Binomial inequality", "type": "Algebra"}
]

# Function to check the answer
def check_answer(guess, formula):
    return guess.strip().lower() == formula.strip().lower()

# Function to evaluate mathematical expressions
def calculate_expression(expression):
    try:
        result = eval(expression, {"__builtins__": None}, {
            "sin": math.sin, "cos": math.cos, "tan": math.tan,
            "pi": math.pi, "e": math.e, "sqrt": math.sqrt, "log": math.log, "exp": math.exp
        })
        return result
    except Exception as e:
        return f"Error: {e}"

# Function to provide hints
def get_hint(formula, attempts):
    hints = [
        f"The formula has {len(formula)} characters.",
        f"The formula starts with: {formula[0]}.",
        f"The formula ends with: {formula[-1]}.",
        f"The formula contains the following symbols: {' '.join(set(filter(lambda c: not c.isalnum(), formula)))}."
    ]
    return hints[min(attempts - 1, len(hints) - 1)]

# Main CLI program
def main():
    while True:
        print("\nChoose an option:")
        print("1. Play the guessing game")
        print("2. Use the calculator")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            # Guessing game
            current_formula = random.choice(functions)
            attempts = 0
            max_attempts = 5
            print(f"\nUse: {current_formula['use']}\nType: {current_formula['type']}")

            while attempts < max_attempts:
                guess = input(f"Attempt {attempts + 1}/{max_attempts} - Guess the formula: ")
                if check_answer(guess, current_formula['formula']):
                    print("\033[32m✓ Correct! You guessed the formula.\033[0m")
                    break
                else:
                    attempts += 1
                    print(f"\033[31m❌ Incorrect. Hint: {get_hint(current_formula['formula'], attempts)}\033[0m")

            if attempts == max_attempts:
                print(f"\033[31mSorry, you've used all attempts. The correct formula was: {current_formula['formula']}\033[0m")

        elif choice == "2":
            # Calculator
            expression = input("Enter a mathematical expression: ")
            result = calculate_expression(expression)
            print(f"Result: {result}")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
