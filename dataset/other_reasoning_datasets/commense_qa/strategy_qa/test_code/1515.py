def solution():
    ny_winter_temp_range = range(12, 31)
    fl_winter_temp_range = range(65, 78)
    if min(ny_winter_temp_range) < min(fl_winter_temp_range):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())