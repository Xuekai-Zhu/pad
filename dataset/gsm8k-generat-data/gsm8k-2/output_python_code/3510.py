def solution():
    """Victoria had $500. She went to the market and bought 2 packets of rice each at $20, 3 packets of wheat flour each at $25, and 1 soda at $150. What was her remaining balance?"""
    starting_balance = 500
    rice_cost = 20
    wheat_flour_cost = 25
    soda_cost = 150
    rice_quantity = 2
    wheat_flour_quantity = 3
    total_cost = (rice_cost * rice_quantity) + (wheat_flour_cost * wheat_flour_quantity) + soda_cost
    remaining_balance = starting_balance - total_cost
    result = remaining_balance
    return result

print(solution())