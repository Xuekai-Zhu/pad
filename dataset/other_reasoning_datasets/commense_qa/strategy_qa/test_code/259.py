def solution():
    diamond_density = 3.51
    water_density = 997.0
    if diamond_density > water_density:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())