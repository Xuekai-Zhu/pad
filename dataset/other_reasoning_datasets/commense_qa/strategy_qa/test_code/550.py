def solution():
    cat_weight_range = range(7,11)
    curiosity_weight = 1982
    for weight in cat_weight_range:
        force = curiosity_weight * 9.8 # acceleration due to gravity on Earth
        if force >= weight:
            result = "yes"
            break
        else:
            result = "no"
    return result

print(solution())