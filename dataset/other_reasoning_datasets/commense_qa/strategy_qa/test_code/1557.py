def solution():
    voyager_distance = 12161300000
    hwasong_range = 8000
    if hwasong_range >= voyager_distance:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())