def solution():
    """Dr. Jones earns $6,000 a month. His house rental is $640 each month; his monthly food expense is $380; his electric and water bill costs 1/4 of what he makes, and his insurances cost 1/5 of what he makes. How much money does he have left after paying those four bills?"""
    monthly_income = 6000
    rental_expense = 640
    food_expense = 380
    electric_water_expense = monthly_income * 0.25
    insurance_expense = monthly_income * 0.2
    total_expenses = rental_expense + food_expense + electric_water_expense + insurance_expense
    remaining_income = monthly_income - total_expenses
    result = remaining_income
    return result

print(solution())