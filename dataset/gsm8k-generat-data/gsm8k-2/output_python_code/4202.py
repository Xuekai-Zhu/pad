def solution():
    """Kyle makes $3200.00 every month. His monthly bills include $1250 for rent, $150 on utilities, $400 into retirement & savings accounts, $300.00 on groceries/eating out, $200 for insurance and $200 for miscellaneous expenses. If he’s looking at buying a car with a monthly car payment of $350 how much does that leave for gas and maintenance?"""
    monthly_income = 3200
    monthly_bills = 1250 + 150 + 400 + 300 + 200 + 200
    car_payment = 350
    remaining_money = monthly_income - monthly_bills - car_payment
    result = remaining_money
    return result

print(solution())