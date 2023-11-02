def solution():
    # Calculate the amount of money spent on food
    rent = 600
    food = (3/5) * rent

    # Calculate the amount of money spent on the mortgage bill
    mortgage = 3 * food

    # Calculate the total expenses
    total_expenses = rent + food + mortgage

    # Calculate the amount of taxes paid
    savings = 2000
    taxes = (2/5) * savings

    # Calculate the gross monthly salary
    gross_salary = total_expenses + taxes
    result = gross_salary
    return result

print(solution())