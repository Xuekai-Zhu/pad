def solution():
    chickens = 20
    eggs_per_chicken = 6
    eggs_per_carton = 12
    total_eggs = chickens * eggs_per_chicken
    cartons = total_eggs / eggs_per_carton
    result = cartons
    return result

print(solution())