def solution():
    location = "Quahog, Rhode Island"
    west_coast = False
    if "West Coast" in location:
        west_coast = True
    if west_coast:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())