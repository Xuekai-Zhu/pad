def solution():
    """Mrs. Petersons bought 10 tumblers for $45 each. She paid with five $100 bills. How much change will Mrs. Petersons receive?"""
    tumbler_price = 45
    num_tumblers = 10
    total_cost = tumbler_price * num_tumblers
    amount_paid = 5 * 100
    change = amount_paid - total_cost
    result = change
    return result

print(solution())