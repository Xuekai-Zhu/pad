def solution():
    candy_price = 1
    candy_weight = 12  # ounces per bag of candy

    chips_price = 1.4
    chips_weight = 17  # ounces per bag of chips

    budget = 7

    # Calculate how many bags of candy Amber can buy
    num_candy_bags = budget // candy_price

    # Calculate how many ounces of candy Amber can get
    total_candy_weight = num_candy_bags * candy_weight

    # Calculate how many bags of chips Amber can buy
    num_chips_bags = budget // chips_price

    # Calculate how many ounces of chips Amber can get
    total_chips_weight = num_chips_bags * chips_weight

    # Compare the total weights and return the larger amount
    result = max(total_candy_weight, total_chips_weight)
    return result

print(solution())