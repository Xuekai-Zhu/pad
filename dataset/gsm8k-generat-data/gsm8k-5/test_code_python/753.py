def solution():
    bags_morning = 29  # The shop sold 29 bags of potatoes in the morning
    bags_afternoon = 17  # The shop sold 17 bags of potatoes in the afternoon
    weight_per_bag = 7  # Each bag of potatoes weighs 7kg

    # Calculate the total weight of potatoes sold in the morning
    weight_morning = bags_morning * weight_per_bag

    # Calculate the total weight of potatoes sold in the afternoon
    weight_afternoon = bags_afternoon * weight_per_bag

    # Calculate the total weight of potatoes sold for the whole day
    total_weight = weight_morning + weight_afternoon
    result = total_weight
    return result

print(solution())