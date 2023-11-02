def solution():
    pottery_kiln_heat_source = "sides"
    glass_kiln_heat_source = "top"
    if pottery_kiln_heat_source != glass_kiln_heat_source:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())