def solution():
    gladiator_timespan = range(-1000, 500)
    shotgun_invention_year = 1700
    if shotgun_invention_year > max(gladiator_timespan):
        result = "no"
    else:
        result = "Cannot determine"
    return result

print(solution())