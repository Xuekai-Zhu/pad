def solution():
    # Calculate the total cost of replacing the floor
    room_area = 8 * 7  # area of Tom's room
    new_floor_cost = room_area * 1.25  # cost of the new floor per square foot
    total_cost = 50 + new_floor_cost  # cost to remove old floor plus cost of new floor
    result = total_cost
    return result

print(solution())