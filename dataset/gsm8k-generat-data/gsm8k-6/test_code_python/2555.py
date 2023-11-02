def solution():
    # Calculate the total weight of Mars, excluding other elements
    mars_weight = 150 / 0.3  # other elements make up 30% of Mars's weight
    total_weight = mars_weight * 2  # Mars weighs twice as much as the moon

    # Calculate the weight of iron and carbon in the moon
    iron_weight = total_weight * 0.5
    carbon_weight = total_weight * 0.2

    # Calculate the weight of the moon
    moon_weight = iron_weight + carbon_weight
    result = moon_weight
    return result

print(solution())