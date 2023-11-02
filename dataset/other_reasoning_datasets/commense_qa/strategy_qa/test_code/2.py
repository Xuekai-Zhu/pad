def solution():
    # Define the density of a raw pear and the density of water
    pear_density = 0.59
    water_density = 1.0
    # Check if the pear is denser than water
    if pear_density > water_density:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())