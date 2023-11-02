def solution():
    # Volume of each jug: 2 gallons
    volume = 2

    # Amount of sand in each jug: 70% of 2 gallons
    sand_volume = volume * 0.7

    # Density of sand: 5 pounds/gallon
    density = 5

    # Weight of sand in each jug
    weight = sand_volume * density

    # Total weight of both jugs filled with sand
    total_weight = weight * 2
    result = total_weight
    return result

print(solution())