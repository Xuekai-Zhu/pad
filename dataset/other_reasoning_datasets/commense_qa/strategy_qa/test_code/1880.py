def solution():
    years_between_burials = 1995 - 1907
    years_per_neptunian_orbit = 165
    full_orbits = years_between_burials // years_per_neptunian_orbit
    if full_orbits > 0:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())