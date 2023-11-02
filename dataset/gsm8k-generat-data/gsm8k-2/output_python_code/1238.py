def solution():
    """Tom decides to get a new floor for his room. It cost $50 to remove the floor. The new floor costs $1.25 per square foot and Tom's room is 8*7 feet. How much did it cost to replace the floor?"""
    floor_removal_cost = 50
    new_floor_cost_per_sq_ft = 1.25
    room_length = 8
    room_width = 7
    room_area = room_length * room_width
    new_floor_cost = new_floor_cost_per_sq_ft * room_area
    total_cost = floor_removal_cost + new_floor_cost
    result = total_cost
    return result

print(solution())