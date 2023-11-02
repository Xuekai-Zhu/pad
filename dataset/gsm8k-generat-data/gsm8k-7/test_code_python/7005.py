def solution():
    earth_surface_area = 200
    moon_surface_area = earth_surface_area / 5
    earth_land_value = 80 / (6 * earth_surface_area)
    moon_land_value = earth_land_value * 6
    moon_total_value = moon_surface_area * moon_land_value
    result = round(moon_total_value, 2)
    return result

print(solution())