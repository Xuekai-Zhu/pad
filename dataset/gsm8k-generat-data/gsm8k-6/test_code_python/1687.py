def solution():
    # Calculate the total weight of the bags of lemons
    total_weight = 100 * 8  # one bag of lemons has a mass of 8 kilograms
    remaining_weight = 900 - total_weight  # calculate the remaining weight that can be loaded into the truck

    result = remaining_weight
    return result

print(solution())