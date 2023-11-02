def solution():
    """Kyle makes $3200.00 every month. His monthly bills include $1250 for rent, $150 on utilities, $400 into retirement & savings accounts, $300.00 on groceries/eating out, $200 for insurance and $200 for miscellaneous expenses. If he’s looking at buying a car with a monthly car payment of $350 how much does that leave for gas and maintenance?"""
    # Define Kyle's monthly income
    income = 3200

    # Define Kyle's monthly bills
    rent = 1250
    utilities = 150
    retirement_savings = 400
    groceries_eating_out = 300
    insurance = 200
    miscellaneous = 200

    # Calculate Kyle's total monthly bills
    total_bills = rent + utilities + retirement_savings + groceries_eating_out + insurance + miscellaneous

    # Calculate the amount left after paying bills and car payment
    left_over = income - total_bills - 350

    # Display the amount left for gas and maintenance
    result = left_over
    return result

print(solution())