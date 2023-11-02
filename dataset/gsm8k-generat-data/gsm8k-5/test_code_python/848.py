def solution():
    liters_per_cow = 108 / 6  # On average, each cow produces 108/6=18 liters of milk per week
    total_liters = 2160  # The cows produced 2160 liters in five weeks

    # Calculate the total number of cows on the farm
    total_cows = total_liters / (liters_per_cow * 5)

    result = total_cows
    return result

print(solution())