def solution():
    phobos_orbits_around = "Mars"
    mars_is_in_solar_system = True
    solar_system_is_in_milky_way = True
    andromeda_galaxy = "Andromeda"
    if phobos_orbits_around == mars_is_in_solar_system and solar_system_is_in_milky_way and phobos_orbits_around != andromeda_galaxy:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())