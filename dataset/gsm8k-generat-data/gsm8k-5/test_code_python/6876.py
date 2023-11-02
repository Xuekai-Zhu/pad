def solution():
    total_cost = (2 * 24) + (2 * 3.5) + (3 * 2)  # Cost of all the items Selena ordered
    remaining_money = 99 - total_cost  # Amount left after paying for the meal and tip
    result = remaining_money
    return result

print(solution())