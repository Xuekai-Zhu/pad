def solution():
    """Tommy's home is worth 25% more than he bought it for. He sells it and buys a new house that costs $500,000. If he had to take a loan for the 75% he can't pay, how much did he buy his first house for?"""
    new_house_cost = 500000
    percent_paid_by_tommy = 0.25
    loan_percent = 0.75
    loan_amount = new_house_cost * loan_percent
    original_house_cost = loan_amount / percent_paid_by_tommy
    result = original_house_cost
    return result

print(solution())