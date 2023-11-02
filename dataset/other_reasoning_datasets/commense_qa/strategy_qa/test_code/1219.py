def solution():
    spends_time_in_nature = True
    increased_exposure_to_sunlight = True
    increased_vitamin_D_levels = True

    if spends_time_in_nature and increased_exposure_to_sunlight and increased_vitamin_D_levels:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())