def solution():
    """The moon has a surface area that is 1/5 that of Earth. The surface area of the Earth is 200 square acres. The land on the moon is worth 6 times that of the land on the Earth. If the total value of all the land on the earth is 80 billion dollars, what is the total value in billions of all the land on the moon?"""
    earth_surface_area = 200
    moon_surface_area = earth_surface_area / 5
    earth_land_value = 80
    moon_land_value = earth_land_value * 6
    total_value_moon_land = (moon_surface_area / earth_surface_area) * moon_land_value
    result = total_value_moon_land
    return result

print(solution())