def solution():
    children = 100
    cupcakes_needed = children * 1
    packs_of_15 = 4
    cupcakes_from_15 = packs_of_15 * 15
    cupcakes_needed_from_10 = cupcakes_needed - cupcakes_from_15
    packs_of_10 = cupcakes_needed_from_10 / 10
    result = packs_of_10
    
    return result

print(solution())