def solution():
    penguins_are_native_to_southern_hemisphere = True
    Miami_is_in_northern_hemisphere = True
    Miami_climate_is_warm = True
    if penguins_are_native_to_southern_hemisphere and Miami_is_in_northern_hemisphere and not Miami_climate_is_warm:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())