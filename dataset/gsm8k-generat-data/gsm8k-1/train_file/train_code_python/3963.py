def solution():
    """A conference center has six rooms. Each room can hold up to 80 people. Today, the conference center is only 2/3 full. How many people are in the conference center?"""
    room_capacity = 80
    total_capacity = 6 * room_capacity
    percent_full = 2/3
    actual_capacity = percent_full * total_capacity
    result = actual_capacity
    return result

print(solution())