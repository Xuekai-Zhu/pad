def solution():
    # Calculate the cost of the silver
    silver_cost = 1.5 * 20  # $20 per ounce for 1.5 ounces of silver

    # Calculate the cost of twice as much gold
    gold_cost = 2 * 1.5 * 20 * 50  # 50 times more expensive than silver, and John bought twice as much, so 2 * 1.5 * 20 * 50

    # Calculate the total cost
    total_cost = silver_cost + gold_cost
    result = total_cost
    return result

print(solution())