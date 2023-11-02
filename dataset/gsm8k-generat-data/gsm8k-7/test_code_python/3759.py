def solution():
    num_cider = 40
    num_beer = 80
    num_mixture = 180 - num_cider - num_beer
    num_each = (num_cider + num_beer + num_mixture) / 2
    num_first_house = num_each
    result = num_first_house
    return result

print(solution())