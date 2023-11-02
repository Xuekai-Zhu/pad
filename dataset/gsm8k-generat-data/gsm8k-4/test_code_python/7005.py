def solution():
    """The moon has a surface area that is 1/5 that of Earth. The surface area of the Earth is 200 square acres. The land on the moon is worth 6 times that of the land on the Earth. If the total value of all the land on the earth is 80 billion dollars, what is the total value in billions of all the land on the moon?"""
    # Define the surface area of the Earth and the moon
    earth_surface_area = 200
    moon_surface_area = earth_surface_area / 5

    # Calculate the value of one acre of land on Earth
    earth_acre_value = 80 / earth_surface_area

    # Calculate the value of one acre of land on the moon
    moon_acre_value = earth_acre_value * 6

    # Calculate the total value of all the land on the moon
    moon_total_value = moon_acre_value * moon_surface_area

    # return the result
    result = moon_total_value
    return result

print(solution())