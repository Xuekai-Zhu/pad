def solution():
    brake_failure = True
    vehicular_crash = True
    people_die = True
    if brake_failure and vehicular_crash and people_die:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())