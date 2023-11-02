def solution():
    
    sam_hunts = 6
    rob_hunts = sam_hunts / 2
    total_hunts = sam_hunts + rob_hunts
    mark_hunts = total_hunts / 3
    peter_hunts = mark_hunts * 3
    total_animals = sam_hunts + rob_hunts + mark_hunts + peter_hunts
    result = total_animals
    return result

print(solution())