def solution():
    # Define the density of copper and brass and the density of water
    copper_density = 8.96
    brass_density = 8.4
    water_density = 1.0
    # Calculate the density of the 2 Euro coin
    coin_density = (copper_density + brass_density) / 2
    # Check if the coin will float in water
    if coin_density < water_density:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())