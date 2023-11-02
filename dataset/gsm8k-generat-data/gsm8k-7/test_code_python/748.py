def solution():
    total_savings = 80
    earrings_cost = 23
    necklace_cost = 48

    # Calculate the total amount spent on jewelry
    total_jewelry_cost = earrings_cost + necklace_cost

    # Calculate the amount of savings left
    savings_left = total_savings - total_jewelry_cost
    result = savings_left
    return result

print(solution())