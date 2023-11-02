def solution():
    staplers = 50  # total number of staplers
    reports = 3*12  # number of reports to be stapled
    used_staplers = reports//2  # number of staplers used to staple reports
    remaining_staplers = staplers - used_staplers  # number of staplers remaining in the stapler
    result = remaining_staplers
    return result

print(solution())