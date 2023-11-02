def solution():
    columbus_expedition_year = 1492
    durian_origin = "Southeast Asia"
    if columbus_expedition_year < 1800 and durian_origin == "Southeast Asia":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())