def solution():
    # Calculate the surface area of the moon
    moon_surface_area = (1/5) * 200
    # Calculate the value of the land on Earth (per acre)
    earth_value_per_acre = 80/200
    # Calculate the value of the land on the moon (per acre)
    moon_value_per_acre = 6 * earth_value_per_acre
    # Calculate the total value of all the land on the moon
    moon_total_value = moon_surface_area * moon_value_per_acre
    # Convert the total value to billions
    moon_total_value_billions = moon_total_value / 1000
    result = moon_total_value_billions
    return result

print(solution())