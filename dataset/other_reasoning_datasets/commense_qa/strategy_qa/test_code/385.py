def solution():
    woman_birth_time = 9 # months
    wheat_harvest_time = 8 # months
    if woman_birth_time < wheat_harvest_time:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())