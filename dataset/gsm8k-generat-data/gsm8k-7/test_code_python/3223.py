def solution():
    total_chickens = 9000
    rooster_to_hen_ratio = 2/1

    # Calculate the total number of hens
    num_hens = total_chickens / (1 + rooster_to_hen_ratio)

    # Calculate the total number of roosters
    num_roosters = rooster_to_hen_ratio * num_hens

    result = num_roosters
    return result

print(solution())