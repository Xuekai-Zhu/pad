def solution():
    robotics_company_formed = 1950
    wall_street_crash = 1929
    if wall_street_crash < robotics_company_formed:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())