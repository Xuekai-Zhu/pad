def solution():
    """Tom decides to get a new floor for his room. It cost $50 to remove the floor. The new floor costs $1.25 per square foot and Tom's room is 8*7 feet. How much did it cost to replace the floor?"""
    # Define the dimensions of Tom's room and the cost per square foot of the new floor
    room_length = 8
    room_width = 7
    cost_per_square_foot = 1.25

    # Calculate the total area of the room
    room_area = room_length * room_width

    # Calculate the cost of the new floor
    new_floor_cost = room_area * cost_per_square_foot

    # Add the cost of removing the old floor
    total_cost = new_floor_cost + 50

    result = total_cost
    return result

print(solution())