def solution():
    number_of_animated_bandmates = 4
    number_of_actual_band_members = 3
    if number_of_animated_bandmates > number_of_actual_band_members:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())