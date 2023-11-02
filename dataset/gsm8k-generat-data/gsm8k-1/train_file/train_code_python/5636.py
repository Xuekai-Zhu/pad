def solution():
    """Mrs. Petersons bought 10 tumblers for $45 each. She paid with five $100 bills. How much change will Mrs. Petersons receive?"""
    num_tumblers = 10
    price_per_tumbler = 45
    total_cost = num_tumblers * price_per_tumbler
    amount_paid = 500
    change = amount_paid - total_cost
    result = change
    return result

print(solution())