def solution():
    
    sam_hunts = 6
    rob_hunts = sam_hunts / 2
    total_hunts = sam_hunts + rob_hunts
    mark_hunts = total_hunts / 3
    peter_hunts = 3 * mark_hunts
    total_animals_hunted = sam_hunts + rob_hunts + mark_hunts + peter_hunts
    result = total_animals_hunted
    return result

print(solution())