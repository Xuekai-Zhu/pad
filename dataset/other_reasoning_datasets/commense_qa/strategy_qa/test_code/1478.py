def solution():
    abyssal_plain_depth_range = (10000, 20000)
    goat_living_habitat = "land"
    if goat_living_habitat != "water" and abyssal_plain_depth_range[0] <= 0:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())