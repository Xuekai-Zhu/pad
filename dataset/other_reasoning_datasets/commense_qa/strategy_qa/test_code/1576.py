def solution():
    earth_orbit_days = 365
    napoleonic_war_days = (12*365) + (5*30) + (4*7)
    if napoleonic_war_days >= earth_orbit_days:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())