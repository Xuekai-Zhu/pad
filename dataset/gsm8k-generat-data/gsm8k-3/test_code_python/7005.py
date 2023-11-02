def solution():
    """The moon has a surface area that is 1/5 that of Earth. The surface area of the Earth is 200 square acres. The land on the moon is worth 6 times that of the land on the Earth. If the total value of all the land on the earth is 80 billion dollars, what is the total value in billions of all the land on the moon?"""
    # Define the surface area of the Earth and the moon
    EARTH_AREA = 200
    MOON_AREA = EARTH_AREA * (1/5)

    # Define the value of land on Earth and the moon
    EARTH_VALUE = 80
    MOON_VALUE = EARTH_VALUE * 6

    # Calculate the total value of all land on the moon
    total_value = MOON_AREA / EARTH_AREA * MOON_VALUE

    # Display the total value
    result = total_value
    return result

print(solution())