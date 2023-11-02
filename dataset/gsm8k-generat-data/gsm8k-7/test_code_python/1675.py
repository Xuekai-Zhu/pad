def solution():
    lorry_weight = 500
    num_bags = 20
    weight_per_bag = 60

    # Calculate the total weight of all the bags of apples
    total_weight = num_bags * weight_per_bag

    # Calculate the new weight of the lorry
    new_weight = lorry_weight + total_weight
    result = new_weight
    return result

print(solution())