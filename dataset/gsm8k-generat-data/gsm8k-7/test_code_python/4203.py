def solution():
    monthly_income = 3200.0
    rent = 1250.0
    utilities = 150.0
    retirement_savings = 400.0
    groceries_eating_out = 300.0
    insurance = 200.0
    misc_expenses = 200.0
    car_payment = 350.0
    
    # Calculate the total monthly expenses
    total_expenses = rent + utilities + retirement_savings + groceries_eating_out + insurance + misc_expenses + car_payment
    
    # Calculate the amount left over for gas and maintenance
    left_over = monthly_income - total_expenses
    result = left_over
    return result

print(solution())