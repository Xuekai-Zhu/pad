def solution():
    total_chickens = 9000
    ratio_roosters_to_hens = 2
    number_of_hens = total_chickens / (ratio_roosters_to_hens + 1)
    number_of_roosters = total_chickens - number_of_hens
    result = number_of_roosters
    return result

print(solution())