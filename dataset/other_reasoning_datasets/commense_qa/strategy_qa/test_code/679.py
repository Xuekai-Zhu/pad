def solution():
    telescope_observes = "outer space"
    largest_mountain_location = "underneath the ocean"
    if largest_mountain_location not in telescope_observes:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())