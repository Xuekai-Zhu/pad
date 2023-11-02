def solution():
    length = 220
    width = 120
    tilled_land = length * width * 0.5
    trellises = length * width * 0.333
    raised_beds = length * width - tilled_land - trellises
    result = raised_beds
    return result

print(solution())