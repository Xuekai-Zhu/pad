def solution():
    mercury_density = 13.56
    penny_density = 7.15
    if penny_density < mercury_density:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())