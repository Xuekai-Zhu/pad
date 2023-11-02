def solution():
    arctic_temp_range = (-36.4, 50)
    sonoran_temp_range = (32.2, 118)
    if sonoran_temp_range[1] < arctic_temp_range[0] or sonoran_temp_range[0] > arctic_temp_range[1]:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())