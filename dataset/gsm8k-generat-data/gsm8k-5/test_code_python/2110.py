def solution():
    snickers_cost = 1.5  # Each piece of Snickers costs $1.5
    mm_cost = 3 * snickers_cost / 2  # A pack of M&M's has the same cost as 2 Snickers

    total_cost = 2 * snickers_cost + 3 * mm_cost  # Calculate the total cost of the items
    paid_amount = 20  # Julia gave the cashier 2 $10 bills
    change = paid_amount - total_cost  # Calculate the change

    result = change
    return result

print(solution())