def solution():
    total_chickens = 75  # There are 75 total chickens on the farm
    roosters = (total_chickens + 5) / 10  # The number of roosters is (total + 5)/10
    hens = total_chickens - roosters  # The number of hens is the total minus the number of roosters

    result = hens
    return result

print(solution())