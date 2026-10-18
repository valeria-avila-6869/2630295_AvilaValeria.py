"""
Manejo de nùmeros y booleanos en Python
2630295
Valeria Alejandra Avila Ponce
I M1-2
"""
# Problem 1: Temperature converter and range flag
# Description:
# Convert Celsius to Fahrenheit and Kelvin. Flag temperatures that are
# greater than or equal to 30 Celsius.
# Inputs: temp_c (float, Celsius).
# Outputs: Fahrenheit, Kelvin, and High temperature (true/false).
# Validations: Input must be numeric; Kelvin must not be below 0.
# Test cases:
# 1) Normal: 25 -> Fahrenheit 77, Kelvin 298.15, High temperature False.
# 2) Border: -273.15 -> Fahrenheit -459.67, Kelvin 0, High temperature False.
# 3) Error: -300 -> Error because Kelvin would be below 0.

def problem_1():
    try:
        temp_c = float(input("Enter temperature in Celsius: "))
        temp_f = temp_c * 9 / 5 + 32
        temp_k = temp_c + 273.15

        if temp_k < 0.0:
            print("Error: invalid input")
            return

        is_high_temperature = temp_c >= 30.0
        print("Fahrenheit:", round(temp_f, 2))
        print("Kelvin:", round(temp_k, 2))
        print("High temperature:", str(is_high_temperature).lower())
    except ValueError:
        print("Error: invalid input")

# Problem 2: Work hours and overtime payment
# Description:
# Calculate weekly pay. Up to 40 hours are paid at the regular rate;
# additional hours are paid at 150% of the regular hourly rate.
# Inputs: hours_worked (float), hourly_rate (float).
# Outputs: Regular pay, Overtime pay, Total pay, Has overtime (true/false).
# Validations: hours_worked >= 0 and hourly_rate > 0.
# Test cases:
# 1) Normal: 45 hours at 20 -> regular 800, overtime 150, total 950, True.
# 2) Border: 40 hours at 20 -> regular 800, overtime 0, total 800, False.
# 3) Error: -2 hours at 20 -> Error: invalid input.

def problem_2():
    try:
        hours_worked = float(input("Enter hours worked this week: "))
        hourly_rate = float(input("Enter hourly rate: "))

        if hours_worked < 0 or hourly_rate <= 0:
            print("Error: invalid input")
            return

        regular_hours = min(hours_worked, 40.0)
        overtime_hours = max(hours_worked - 40.0, 0.0)
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = hours_worked > 40.0

        print("Regular pay:", round(regular_pay, 2))
        print("Overtime pay:", round(overtime_pay, 2))
        print("Total pay:", round(total_pay, 2))
        print("Has overtime:", str(has_overtime).lower())
    except ValueError:
        print("Error: invalid input")

# Problem 3: Discount eligibility with booleans
# Description:
# A customer qualifies for a 10% discount if they are a student, a senior,
# or their purchase is at least 1000.00.
# Inputs: purchase_total (float), is_student_text (YES/NO), is_senior_text (YES/NO).
# Outputs: Discount eligible (true/false), Final total.
# Validations: Purchase total >= 0; answers must be YES or NO (case-insensitive).
# Test cases:
# 1) Normal: 500, YES, NO -> eligible True, final total 450.
# 2) Border: 1000, NO, NO -> eligible True, final total 900.
# 3) Error: 500, MAYBE, NO -> Error: invalid input.

def problem_3():
    try:
        purchase_total = float(input("Enter purchase total: "))
        is_student_text = input("Is the customer a student? (YES/NO): ").strip().upper()
        is_senior_text = input("Is the customer a senior? (YES/NO): ").strip().upper()

        if purchase_total < 0 or is_student_text not in ("YES", "NO") or is_senior_text not in ("YES", "NO"):
            print("Error: invalid input")
            return

        is_student = is_student_text == "YES"
        is_senior = is_senior_text == "YES"
        discount_eligible = is_student or is_senior or purchase_total >= 1000.0

        if discount_eligible:
            final_total = purchase_total * 0.9
        else:
            final_total = purchase_total

        print("Discount eligible:", str(discount_eligible).lower())
        print("Final total:", round(final_total, 2))
    except ValueError:
        print("Error: invalid input")


# Problem 4: Basic statistics of three integers
# Description:
# Read three integers and calculate their sum, average, maximum, minimum,
# and whether all three numbers are even.
# Inputs: n1, n2, n3 (integers; negative values are allowed).
# Outputs: Sum, Average, Max, Min, All even (true/false).
# Validations: Each input must be convertible to int.
# Test cases:
# 1) Normal: 2, 4, 6 -> sum 12, average 4, max 6, min 2, True.
# 2) Border: 0, -2, 2 -> sum 0, average 0, max 2, min -2, True.
# 3) Error: 2, "abc", 6 -> Error: invalid input.


def problem_4():
    try:
        n1 = int(input("Enter the first integer: "))
        n2 = int(input("Enter the second integer: "))
        n3 = int(input("Enter the third integer: "))

        sum_value = n1 + n2 + n3
        average_value = sum_value / 3
        max_value = max(n1, n2, n3)
        min_value = min(n1, n2, n3)
        all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

        print("Sum:", sum_value)
        print("Average:", round(average_value, 2))
        print("Max:", max_value)
        print("Min:", min_value)
        print("All even:", str(all_even).lower())
    except ValueError:
        print("Error: invalid input")

# Problem 5: Loan eligibility (income and debt ratio)
# Description:
# Determine loan eligibility using monthly income, monthly debt, and credit score.
# Eligibility requires income >= 8000, debt ratio <= 0.4, and score >= 650.
# Inputs: monthly_income (float), monthly_debt (float), credit_score (int).
# Outputs: Debt ratio, Eligible (true/false).
# Validations: Income > 0, debt >= 0, score >= 0; no division by zero.
# Test cases:
# 1) Normal: income 10000, debt 3000, score 700 -> ratio 0.3, True.
# 2) Border: income 8000, debt 3200, score 650 -> ratio 0.4, True.
# 3) Error: income 0, debt 100, score 700 -> Error: invalid input.

def problem_5():
    try:
        monthly_income = float(input("Enter monthly income: "))
        monthly_debt = float(input("Enter monthly debt payments: "))
        credit_score = int(input("Enter credit score: "))

        if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
            print("Error: invalid input")
            return

        debt_ratio = monthly_debt / monthly_income
        eligible = (
            monthly_income >= 8000.0
            and debt_ratio <= 0.4
            and credit_score >= 650
        )

        print("Debt ratio:", round(debt_ratio, 2))
        print("Eligible:", str(eligible).lower())
    except ValueError:
        print("Error: invalid input")


# Problem 6: Body Mass Index (BMI) and category flag
# Description:
# Calculate BMI using weight in kilograms divided by height in meters squared.
# Classify the result as underweight, normal, or overweight using the assignment's ranges.
# Inputs: weight_kg (float), height_m (float).
# Outputs: BMI (2 decimals), Underweight, Normal, Overweight (true/false).
# Validations: weight_kg > 0 and height_m > 0.
# Test cases:
# 1) Normal: 68 kg, 1.75 m -> BMI about 22.20, Normal True.
# 2) Border: 50 kg, 1.64 m -> BMI about 18.59, Normal True.
# 3) Error: 60 kg, 0 m -> Error: invalid input.


def problem_6():
    try:
        weight_kg = float(input("Enter weight in kilograms: "))
        height_m = float(input("Enter height in meters: "))

        if weight_kg <= 0 or height_m <= 0:
            print("Error: invalid input")
            return

        bmi = weight_kg / (height_m * height_m)
        is_underweight = bmi < 18.5
        is_normal = 18.5 <= bmi < 25.0
        is_overweight = bmi >= 25.0

        print("BMI:", round(bmi, 2))
        print("Underweight:", str(is_underweight).lower())
        print("Normal:", str(is_normal).lower())
        print("Overweight:", str(is_overweight).lower())
    except ValueError:
        print("Error: invalid input")
        
# MAIN MENU
# Select one of the six problems to run.

def main():
    problems = {
        "1": problem_1,
        "2": problem_2,
        "3": problem_3,
        "4": problem_4,
        "5": problem_5,
        "6": problem_6,
    }

    print("Numeric Types and Boolean Values")
    print("1. Temperature converter")
    print("2. Work hours and overtime payment")
    print("3. Discount eligibility")
    print("4. Statistics of three integers")
    print("5. Loan eligibility")
    print("6. BMI and category")
    choice = input("Choose a problem (1-6): ").strip()

    if choice in problems:
        problems[choice]()
    else:
        print("Error: invalid input")


if __name__ == "__main__":
    main()

# CONCLUSIONS
# Integers and floating-point numbers work together in practical calculations.
# Comparisons create boolean values that allow programs to make decisions.
# Input validation prevents invalid values from producing incorrect results.
# Checking that a divisor is not zero prevents division errors.
# The and, or, and not operators combine conditions to express decision rules.
# Similar patterns can be used in payroll, discounts, loan screening, and measurements.
# Testing normal, border, and invalid cases makes a program more reliable.

# REFERENCES
# 1. Python Software Foundation. Built-in Types:
#    https://docs.python.org/3/library/stdtypes.html
# 2. Python Software Foundation. Numeric Types — int, float, complex:
#    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
# 3. Python Software Foundation. Boolean Type — bool:
#    https://docs.python.org/3/library/stdtypes.html#boolean-type-bool
# 4. Python Software Foundation. Built-in Functions (int, float, min, max, round):
#    https://docs.python.org/3/library/functions.html
# 5. Python Software Foundation. Errors and Exceptions:
#    https://docs.python.org/3/tutorial/errors.html
# 6. Python Software Foundation. More Control Flow Tools:
#    https://docs.python.org/3/tutorial/controlflow.html
