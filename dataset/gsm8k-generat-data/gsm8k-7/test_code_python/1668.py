def solution():
    rock_weight = 1.5  # in pounds
    price_per_pound = 4  # in dollars
    total_sale = 60  # in dollars

    # Calculate the total weight of rocks in pounds
    total_weight = total_sale / price_per_pound

    # Calculate the total number of rocks in the pail
    num_rocks = total_weight / rock_weight
    result = num_rocks
    return result

print(solution())