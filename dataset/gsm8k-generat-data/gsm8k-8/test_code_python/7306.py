def solution():
    # Calculate the total cost of the lemonades and sandwiches
    lemonade_cost = 2 * 2
    sandwich_cost = 2 * 2.5
    total_cost = lemonade_cost + sandwich_cost

    # Calculate the amount of change from a $20 bill
    change = 20 - total_cost
    result = change
    return result

print(solution())