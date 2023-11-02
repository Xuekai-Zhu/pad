def solution():
    # Calculate the total cost of Danny's order
    total_cost = 2 * 3.20 + 2 * 1.90 + 2 * 2.40  # cost of 2 burgers, 2 fries, and 2 milkshakes
    # Calculate how much more Danny needs to spend to avail of free delivery
    if total_cost >= 18:
        more_needed = 0
    else:
        more_needed = 18 - total_cost
    result = more_needed
    return result

print(solution())