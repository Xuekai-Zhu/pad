def solution():
    includes_STI_screenings = True
    increase_testing = True
    if includes_STI_screenings and increase_testing:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())