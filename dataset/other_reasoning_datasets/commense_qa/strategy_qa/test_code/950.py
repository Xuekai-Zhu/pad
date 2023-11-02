def solution():
    jalapeno_heat = 3600
    ghost_pepper_heat = 1000000
    if jalapeno_heat < ghost_pepper_heat:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())