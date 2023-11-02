def solution():
    sam_hunts = 6
    rob_hunts = sam_hunts / 2
    total_rob_sam = sam_hunts + rob_hunts
    mark_hunts = total_rob_sam / 3
    peter_hunts = mark_hunts * 3

    # Calculate the total number of animals they all hunt in a day
    total_hunts = sam_hunts + rob_hunts + mark_hunts + peter_hunts
    result = total_hunts
    return result

print(solution())