def solution():
    austrian_casualties = 373588
    IMS_capacity = 400000
    if austrian_casualties <= IMS_capacity:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())