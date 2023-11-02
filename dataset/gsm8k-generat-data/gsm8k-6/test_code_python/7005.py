def solution():
    # Calculate the surface area of the moon and the value of the land on the Earth
    surface_area_moon = (1/5) * 200  # surface area of the moon is 1/5 that of Earth
    value_land_earth = 80  # total value of all the land on the Earth is 80 billion dollars

    # Calculate the total value of all the land on the moon
    value_land_moon = 6 * value_land_earth * (surface_area_moon / 200)
    result = value_land_moon
    return result

print(solution())