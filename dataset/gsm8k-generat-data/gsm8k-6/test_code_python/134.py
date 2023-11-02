def solution():
    # Calculate the total cost of tickets for the family
    total_cost = 109 * 2  # 2 regular tickets for the adults
    total_cost += (6 - 5) + (10 - 5)  # $5 discount for each child
    # Calculate the change they will receive
    change = 500 - total_cost
    result = change
    return result

print(solution())