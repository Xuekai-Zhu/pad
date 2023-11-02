def solution():
    hourly_rate = 30
    weekly_hours = 48
    monthly_rent_ratio = 1/3
    monthly_food_cost = 500
    monthly_tax_cost = 1000

    # Calculate the firefighter's monthly salary
    monthly_salary = hourly_rate * weekly_hours * 4

    # Calculate the monthly rent cost
    monthly_rent_cost = monthly_salary * monthly_rent_ratio

    # Calculate the total monthly expenses
    total_expenses = monthly_rent_cost + monthly_food_cost + monthly_tax_cost

    # Calculate the amount of money left after paying monthly expenses
    money_left = monthly_salary - total_expenses
    result = money_left
    return result

print(solution())