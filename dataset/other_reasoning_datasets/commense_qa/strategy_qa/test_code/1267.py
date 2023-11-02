def solution():
    shotgun_inventor = "Daniel LeFever"
    cause_of_death = "suicide with a shotgun"
    if shotgun_inventor in cause_of_death:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())