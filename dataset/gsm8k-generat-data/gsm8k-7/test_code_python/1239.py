def solution():
    floor_removal_cost = 50
    new_floor_cost_per_sq_ft = 1.25
    room_length = 8
    room_width = 7

    # Calculate the area of the room
    room_area = room_length * room_width

    # Calculate the cost of the new floor
    new_floor_cost = room_area * new_floor_cost_per_sq_ft

    # Calculate the total cost of replacing the floor
    total_cost = floor_removal_cost + new_floor_cost
    result = total_cost
    return result

print(solution())