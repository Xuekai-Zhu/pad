def solution():
    
    total_income = 2500
    rent = 700
    car_payment = 300
    utilities = car_payment / 2
    groceries = 50
    total_expenses = rent + car_payment + utilities + groceries
    remaining_income = total_income - total_expenses
    retirement_savings = remaining_income / 2
    remaining_money = remaining_income - retirement_savings
    result = remaining_money
    return result

print(solution())