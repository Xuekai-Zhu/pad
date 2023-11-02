def solution():
    """Tommy's home is worth 25% more than he bought it for. He sells it and buys a new house that costs $500,000. If he had to take a loan for the 75% he can't pay, how much did he buy his first house for?"""
    new_house_cost = 500000
    loan_percent = 75
    down_payment_percent = 100 - loan_percent
    old_house_increase = 25
    old_house_cost = new_house_cost * (down_payment_percent / 100) / (1 + old_house_increase / 100)
    result = old_house_cost
    return result

print(solution())