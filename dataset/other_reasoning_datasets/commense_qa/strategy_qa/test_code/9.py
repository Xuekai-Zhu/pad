def solution():
    us_user_percentage = 55
    states_with_pledge_requirement = 45
    if us_user_percentage > states_with_pledge_requirement:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())