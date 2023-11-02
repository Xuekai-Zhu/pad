def solution():
    # Sam hunts 6 animals in a day
    sam_hunts = 6

    # Rob hunts half as many animals as Sam
    rob_hunts = sam_hunts / 2

    # Mark hunts 1/3 of the total animals Rob and Sam hunt
    total_hunted = sam_hunts + rob_hunts
    mark_hunts = total_hunted / 3

    # Peter hunts 3 times as many animals as Mark
    peter_hunts = mark_hunts * 3

    # Calculate the total number of animals they all hunt in a day
    total_animals_hunted = sam_hunts + rob_hunts + mark_hunts + peter_hunts
    result = total_animals_hunted
    return result

print(solution())