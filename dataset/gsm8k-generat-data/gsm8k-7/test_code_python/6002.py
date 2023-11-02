def solution():
    rent = 1200
    food_travel = 2400   # 1/2 of monthly expenses
    total_expenses = rent + food_travel
    shared_rent = rent / 2
    monthly_income = 5000

    # Calculate the amount of money remaining after expenses
    remaining_money = monthly_income - total_expenses + shared_rent
    result = remaining_money
    return result

print(solution())