def solution():
    goofy_creation_year = 1932
    pluto_discovery_year = 1930
    planets_in_1932 = 8 # Pluto was later reclassified as a dwarf planet in 2006
    if goofy_creation_year == pluto_discovery_year and planets_in_1932 == 9:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())