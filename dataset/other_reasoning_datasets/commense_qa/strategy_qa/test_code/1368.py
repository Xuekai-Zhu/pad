def solution():
    parsley_density = 0.26
    milk_density = 1.026
    if parsley_density > milk_density:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())