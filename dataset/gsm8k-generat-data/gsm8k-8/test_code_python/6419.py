def solution():
    # Calculate the cost per ounce for candy and chips
    candy_cost_per_ounce = 1 / 12
    chip_cost_per_ounce = 1.4 / 17

    if candy_cost_per_ounce > chip_cost_per_ounce:
        # If candy is cheaper per ounce, buy candy and calculate the number of ounces
        num_candy_bags = 7
        total_ounces = num_candy_bags * 12
    else:
        # If chips are cheaper per ounce, buy chips and calculate the number of ounces
        num_chip_bags = int(7 / 1.4)
        total_ounces = num_chip_bags * 17

    result = total_ounces
    return result

print(solution())