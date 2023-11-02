def solution():
    bedroom_size = 309
    bathroom_size = 150
    desired_ratio = 2
    new_room_size = desired_ratio * (bedroom_size + bathroom_size)
    result = new_room_size
    return result

print(solution())