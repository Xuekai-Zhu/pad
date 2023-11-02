def solution():
    aerosmith_members = 5
    carpool_min_occupants = 2
    if aerosmith_members >= carpool_min_occupants:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())