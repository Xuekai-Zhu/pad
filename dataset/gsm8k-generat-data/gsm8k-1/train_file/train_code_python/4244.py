def solution():
    """In a day, Sam hunts 6 animals. Rob hunts half as many animals as Sam. Mark hunts 1/3 of the total of what Rob and Sam hunt. If Peter hunts 3 times as many animals as Mark does, how many animals do they all hunt in a day?"""
    sam_hunts = 6
    rob_hunts = sam_hunts / 2
    total_hunts = sam_hunts + rob_hunts
    mark_hunts = total_hunts / 3
    peter_hunts = 3 * mark_hunts
    total_animals_hunted = sam_hunts + rob_hunts + mark_hunts + peter_hunts
    result = total_animals_hunted
    return result

print(solution())