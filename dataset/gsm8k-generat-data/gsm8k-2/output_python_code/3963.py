def solution():
    """A conference center has six rooms. Each room can hold up to 80 people. Today, the conference center is only 2/3 full. How many people are in the conference center?"""
    room_capacity = 80
    total_capacity = room_capacity * 6
    current_capacity = total_capacity * (2 / 3)
    result = current_capacity
    return result

print(solution())