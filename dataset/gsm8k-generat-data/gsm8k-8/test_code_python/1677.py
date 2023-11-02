def solution():
    # Calculate the total cost of Danny's order
    total_cost = 2*3.20 + 2*1.90 + 2*2.40

    # Calculate the remaining amount needed for free delivery
    remaining_amount = 18 - total_cost

    result = remaining_amount
    return result

print(solution())