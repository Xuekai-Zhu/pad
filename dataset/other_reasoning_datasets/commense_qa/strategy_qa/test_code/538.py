def solution():
    ontario_location = "province of Canada"
    surrounding_oceans = "temperate"
    if surrounding_oceans != "tropical" and ontario_location == "province of Canada":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())