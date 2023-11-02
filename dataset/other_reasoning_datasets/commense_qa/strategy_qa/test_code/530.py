def solution():
    french_revolution_start = 1789
    french_revolution_end = 1799
    eiffel_tower_construction_year = 1888
    if eiffel_tower_construction_year > french_revolution_end:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())