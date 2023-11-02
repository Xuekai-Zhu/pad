def solution():
    num_morning_bags = 29
    num_afternoon_bags = 17
    weight_per_bag = 7

    # Calculate the total number of bags sold for the whole day
    total_bags_sold = num_morning_bags + num_afternoon_bags

    # Calculate the total weight of potatoes sold for the whole day
    total_weight_sold = total_bags_sold * weight_per_bag
    result = total_weight_sold
    return result

print(solution())