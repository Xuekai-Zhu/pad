def solution():
    # Calculate the size of Holden's new room
    bedroom_size = 309  # sq ft
    bathroom_size = 150  # sq ft
    new_size = 2 * (bedroom_size + bathroom_size)  # the new room is twice as large as the bedroom and bathroom combined
    result = new_size
    return result

print(solution())