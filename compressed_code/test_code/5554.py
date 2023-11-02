def solution():
    
    initial_frogs = 5
    tadpoles = 3 * initial_frogs
    mature_frogs = round(tadpoles * (2 / 3))
    total_frogs = initial_frogs + mature_frogs
    surplus_frogs = total_frogs - 8
    result = surplus_frogs if surplus_frogs > 0 else 0
    return result

print(solution())