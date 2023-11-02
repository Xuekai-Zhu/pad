def solution():
    # Calculate the total number of shrimp needed
    total_shrimp = 5 * 40  # 5 shrimp per guest, 40 guests

    # Calculate the total weight of shrimp needed in pounds
    total_weight = total_shrimp / 20  # 20 shrimp per pound

    # Calculate the total cost of shrimp
    cost = total_weight * 17.00  # $17.00 per pound

    result = cost
    return result

print(solution())