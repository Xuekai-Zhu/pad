def solution():
    # Find the number of roosters and hens
    roosters = 80 * (1/4)
    hens = 80 - roosters

    # Find the number of hens that lay eggs
    laying_hens = hens * (3/4)

    # Find the number of chickens that do not lay eggs
    non_laying_chickens = roosters + (hens - laying_hens)

    result = non_laying_chickens
    return result

print(solution())