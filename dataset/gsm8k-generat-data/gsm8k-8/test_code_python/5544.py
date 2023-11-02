def solution():
    # Calculate the total weight of sellable potatoes
    sellable_weight = 6500 - 150

    # Calculate the number of bags needed to package all the potatoes
    num_bags = sellable_weight // 50

    # Calculate the total revenue from selling the potatoes
    total_revenue = num_bags * 72

    result = total_revenue
    return result

print(solution())