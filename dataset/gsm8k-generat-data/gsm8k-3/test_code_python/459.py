def solution():
    """A year ago, the total cost of buying a lawnmower was 2/5 times less than the cost it goes for now.
    If the cost was $1800 a year ago, calculate how much it would cost Mr. Lucian to buy 4 such lawnmowers."""
    # Calculate the current cost of one lawnmower
    current_cost = 1800 * (5/3)

    # Calculate the total cost for four lawnmowers
    total_cost = current_cost * 4

    # Display the total cost for four lawnmowers
    result = total_cost
    return result

print(solution())