def solution():
    candy_cost = 1  # The cost of a bag of candy is $1
    candy_weight = 12  # A bag of candy weighs 12 ounces

    chips_cost = 1.4  # The cost of a bag of chips is $1.40
    chips_weight = 17  # A bag of chips weighs 17 ounces

    # Calculate the number of bags of candy that Amber can buy with her $7
    num_candy_bags = 7 // candy_cost

    # Calculate the total weight of candy that Amber can buy
    total_candy_weight = num_candy_bags * candy_weight

    # Calculate the number of bags of chips that Amber can buy with her $7
    num_chips_bags = 7 // chips_cost

    # Calculate the total weight of chips that Amber can buy
    total_chips_weight = num_chips_bags * chips_weight

    # Decide which item gives Amber the most based on weight
    if total_candy_weight > total_chips_weight:
        result = total_candy_weight
    else:
        result = total_chips_weight

    return result

print(solution())