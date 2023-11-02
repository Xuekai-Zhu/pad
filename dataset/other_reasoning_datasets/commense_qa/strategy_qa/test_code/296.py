def solution():
    helium_density = 0.1785 # kg/m^3 at standard temperature and pressure
    air_density = 1.225 # kg/m^3 at standard temperature and pressure
    if helium_density < air_density:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())