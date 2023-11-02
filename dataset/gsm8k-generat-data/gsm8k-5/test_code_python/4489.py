def solution():
    total_cost = 20 + 36 + 5  # Total cost of cake, bouquet, and balloons
    initial_amount = 50  # Michael has $50
    remaining_amount = initial_amount - total_cost  # Remaining amount after buying cake, bouquet, and balloons
    if remaining_amount >= 0:
        result = 0  # If remaining amount is zero or more, Michael doesn't need more money
    else:
        result = abs(remaining_amount)  # If remaining amount is negative, Michael needs more money
    return result

print(solution())