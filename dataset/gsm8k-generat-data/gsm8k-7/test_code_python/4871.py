def solution():
    num_roosters = 80 * (1/4)
    num_hens = 80 - num_roosters
    num_laying_hens = num_hens * (3/4)
    num_non_laying_hens = num_hens - num_laying_hens
    num_non_laying_chickens = num_roosters + num_non_laying_hens
    result = num_non_laying_chickens
    return result

print(solution())