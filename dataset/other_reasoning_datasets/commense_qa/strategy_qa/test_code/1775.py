def solution():
    hair_structure = "keratin"
    food_additive = "L-cysteine"
    additive_source = "keratin"
    if additive_source == hair_structure:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())