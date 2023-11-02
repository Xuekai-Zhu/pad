def solution():
    rice_cost = 2 * 20  # Victoria bought 2 packets of rice at $20 each
    wheat_flour_cost = 3 * 25  # Victoria bought 3 packets of wheat flour at $25 each
    soda_cost = 150  # Victoria bought 1 soda at $150
    total_cost = rice_cost + wheat_flour_cost + soda_cost  # Calculate the total cost of the items

    remaining_balance = 500 - total_cost  # Calculate Victoria's remaining balance
    result = remaining_balance
    return result

print(solution())