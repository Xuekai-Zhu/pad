def solution():
    water_freezing_point_F = 32
    venus_surface_temp_F = (737 * 1.8) - 459.67
    if venus_surface_temp_F <= water_freezing_point_F:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())