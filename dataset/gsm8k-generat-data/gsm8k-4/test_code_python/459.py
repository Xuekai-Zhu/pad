def solution():
    """A year ago, the total cost of buying a lawnmower was 2/5 times less than the cost it goes for now. If the cost was $1800 a year ago, calculate how much it would cost Mr. Lucian to buy 4 such lawnmowers."""
    # Define the cost of the lawnmower a year ago
    cost_last_year = 1800

    # Calculate the current cost of the lawnmower
    cost_now = cost_last_year / (3/5)

    # Calculate the cost of buying 4 lawnmowers
    cost_4_lawnmowers = cost_now * 4

    result = cost_4_lawnmowers
    return result

print(solution())