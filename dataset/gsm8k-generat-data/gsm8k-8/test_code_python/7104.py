def solution():
    # Calculate the weight of the boxes and crates from yesterday's load
    yesterday_weight = 100 * 100 + 10 * 60

    # Calculate the total weight of the supplies in the truck yesterday
    yesterday_total_weight = yesterday_weight

    # Calculate the total weight of the supplies that can still be loaded in the truck
    remaining_weight = 13500 - yesterday_total_weight

    # Calculate how many bags of 40kg each can be loaded
    bags_weight = 50 * 40
    bags_number = remaining_weight // bags_weight
    result = bags_number
    return result

print(solution())