def solution():
    # Calculate the total weight of sellable potatoes
    sellable_weight = 6500 - 150  # total weight minus damaged weight

    # Calculate the number of bags that can be filled with sellable potatoes
    num_bags = sellable_weight // 50

    # Calculate the total revenue from selling the potatoes
    revenue = num_bags * 72

    result = revenue
    return result

print(solution())