def solution():
    # Calculate the amount of carbon dioxide released by using eight plastic bags per shopping trip
    plastic_bags_CO2 = 8 * (4/16)  # each plastic bag releases 4 ounces of CO2, and there are 16 ounces in a pound

    # Calculate how many shopping trips Marla needs to make to surpass the carbon footprint of the canvas bag
    trips = 600 / plastic_bags_CO2
    result = trips
    return result

print(solution())