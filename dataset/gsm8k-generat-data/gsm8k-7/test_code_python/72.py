def solution():
    length = 4
    width = 6
    height = 3

    # Calculate the volume of the aquarium
    volume = length * width * height

    # Calculate the amount of water left after the cat knocked it over
    water_left = volume / 2

    # Calculate the amount of water Nancy added
    water_added = water_left / 2 * 3

    # Calculate the total amount of water in the aquarium
    total_water = water_left + water_added
    result = total_water
    return result

print(solution())