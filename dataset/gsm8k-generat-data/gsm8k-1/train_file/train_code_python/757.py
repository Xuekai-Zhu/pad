def solution():
    """Faith went to a baking shop and bought flour that cost $5 and a cake stand that costs $28. She then gave the cashier two $20 bills and $3 in loose coins. How much change will she receive?"""
    total_cost = 5 + 28
    amount_paid = 20 * 2 + 3
    change = amount_paid - total_cost
    result = change
    return result

print(solution())