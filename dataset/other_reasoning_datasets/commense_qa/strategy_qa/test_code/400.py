def solution():
    longitude_required = True
    latitude_required = True
    if longitude_required and latitude_required:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())