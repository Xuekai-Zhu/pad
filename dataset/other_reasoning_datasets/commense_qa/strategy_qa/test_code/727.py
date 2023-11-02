def solution():
    max_hamster_lifespan = 3
    leap_year_separation = 4
    if leap_year_separation <= max_hamster_lifespan:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())