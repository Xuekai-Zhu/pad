def solution():
    # Calculate the number of towels Frances has
    mary_to_frances_ratio = 4
    mary_towels = 24
    frances_towels = mary_towels / mary_to_frances_ratio

    # Calculate the weight of one towel in pounds
    total_weight_in_pounds = 60
    total_towels = mary_towels + frances_towels
    weight_per_towel_in_pounds = total_weight_in_pounds / total_towels

    # Convert the weight to ounces
    weight_per_towel_in_ounces = weight_per_towel_in_pounds * 16
    frances_weight = frances_towels * weight_per_towel_in_ounces

    result = frances_weight
    return result

print(solution())