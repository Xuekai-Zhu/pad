def solution():
    # Calculate the total cost of Danny's order
    total_cost = (2 * 3.20) + (2 * 1.90) + (2 * 2.40)

    # Calculate the amount of food Danny needs to order to reach the $18 minimum for free delivery
    remaining_cost = 18 - total_cost

    result = remaining_cost
    return result

print(solution())