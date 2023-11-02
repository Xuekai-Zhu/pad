def solution():
    paris_location = "France"
    bern_location = "Switzerland"
    switzerland_borders = ["France"]
    if paris_location in switzerland_borders and bern_location != paris_location:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())