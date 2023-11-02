def solution():
    # Calculate the total weight of the tomatoes Tommy bought
    total_weight = 3 * 20  # Each crate can hold 20 kilograms

    # Calculate the weight of the rotten tomatoes
    rotten_weight = 3

    # Calculate the weight of the good tomatoes
    good_weight = total_weight - rotten_weight

    # Calculate the revenue from selling the good tomatoes
    revenue = good_weight * 6  # $6 per kilogram

    # Calculate the cost of buying the tomatoes
    cost = 330

    # Calculate the profit from selling the tomatoes
    profit = revenue - cost
    result = profit
    return result

print(solution())