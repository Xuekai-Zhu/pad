def solution():
    # Calculate the weight of the other elements in Mars
    mars_other_weight = 150

    # Calculate the total weight of Mars
    mars_total_weight = mars_other_weight / (1 - 0.5 - 0.2)
    moon_total_weight = mars_total_weight / 2

    # Calculate the weight of iron and carbon in the moon
    moon_iron_weight = moon_total_weight * 0.5
    moon_carbon_weight = moon_total_weight * 0.2

    # Calculate the total weight of the moon
    moon_weight = moon_iron_weight + moon_carbon_weight + mars_other_weight
    result = moon_weight
    return result

print(solution())