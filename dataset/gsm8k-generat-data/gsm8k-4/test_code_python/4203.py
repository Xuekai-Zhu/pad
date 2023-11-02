def solution():
    """Kyle makes $3200.00 every month. His monthly bills include $1250 for rent, $150 on utilities, $400 into retirement & savings accounts, $300.00 on groceries/eating out, $200 for insurance and $200 for miscellaneous expenses. If he’s looking at buying a car with a monthly car payment of $350 how much does that leave for gas and maintenance?"""
    # Define Kyle's monthly income and expenses
    monthly_income = 3200
    rent = 1250
    utilities = 150
    savings = 400
    groceries = 300
    insurance = 200
    miscellaneous = 200

    # Calculate Kyle's total monthly expenses
    total_expenses = rent + utilities + savings + groceries + insurance + miscellaneous

    # Calculate how much Kyle has left over for gas and maintenance after making his car payment
    left_over = monthly_income - total_expenses - 350
    
    result = left_over
    return result

print(solution())