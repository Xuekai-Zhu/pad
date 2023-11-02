def solution():
    sam_animals = 6
    rob_animals = sam_animals / 2
    mark_animals = (rob_animals + sam_animals) / 3
    peter_animals = mark_animals * 3
    total_animals = sam_animals + rob_animals + mark_animals + peter_animals
    result = total_animals
    return result

print(solution())