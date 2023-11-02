def solution():
    num_macaroons = 12
    weight_per_macaroon = 5
    num_bags = 4
    eaten_bag = 1

    # Calculate the total weight of all macaroons before one bag is eaten
    total_weight = num_macaroons * weight_per_macaroon

    # Calculate the weight of one bag of macaroons
    bag_weight = total_weight / num_bags

    # Subtract the weight of the eaten bag from the total weight
    remaining_weight = total_weight - (bag_weight * eaten_bag)
    result = remaining_weight
    return result

print(solution())