def solution():
    """Dr. Jones earns $6,000 a month. His house rental is $640 each month; his monthly food expense is $380; his electric and water bill costs 1/4 of what he makes, and his insurances cost 1/5 of what he makes. How much money does he have left after paying those four bills?"""
    monthly_income = 6000
    rent = 640
    food_expense = 380
    utilities = monthly_income / 4
    insurance = monthly_income / 5
    total_expense = rent + food_expense + utilities + insurance
    money_left = monthly_income - total_expense
    result = money_left
    return result

print(solution())