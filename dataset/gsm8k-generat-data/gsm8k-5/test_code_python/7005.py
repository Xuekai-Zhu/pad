def solution():
    earth_land_value = 80 # Total value of all land on Earth in billions of dollars
    earth_surface_area = 200 # Surface area of Earth in square acres
    moon_surface_area = earth_surface_area / 5 # Surface area of Moon in square acres
    moon_land_value_ratio = 6 # Land on Moon is worth 6 times that of Earth land

    # Calculate the total value of all the land on the moon
    moon_land_value = (moon_surface_area / earth_surface_area) * earth_land_value * moon_land_value_ratio

    result = moon_land_value
    return result

print(solution())