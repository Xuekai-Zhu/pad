def solution():
    bedroom_size = 309  # sq ft
    bathroom_size = 150  # sq ft
    new_room_size = (bedroom_size + bathroom_size) * 2  # the new room is twice as large as the master bedroom and bathroom combined
    result = new_room_size
    return result

print(solution())