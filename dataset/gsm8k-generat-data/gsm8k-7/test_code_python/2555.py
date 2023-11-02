def solution():
    mars_weight = 3  # 50% iron + 20% carbon + 30% other elements = 3 parts
    moon_weight = mars_weight / 2
    moon_other_elements = moon_weight * 0.3  # 30% of moon's weight is other elements
    moon_weight -= moon_other_elements / 0.5  # Calculate moon's weight excluding other elements
    result = moon_weight
    return result

print(solution())