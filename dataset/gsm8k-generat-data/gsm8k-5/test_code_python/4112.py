def solution():
    average_bacon_weight = 20  # A pig on average yields 20 pounds of bacon
    bacon_price = 6  # Each pound of bacon is sold for $6 at the farmer's market
    runt_factor = 0.5  # This month's pig is a runt that grew to only half the size of the average pig

    # Calculate the weight of bacon the runt pig will yield
    runt_bacon_weight = average_bacon_weight * runt_factor

    # Calculate the total amount of money the farmer will make from the runt pig's bacon
    total_money = runt_bacon_weight * bacon_price
    result = total_money
    return result

print(solution())