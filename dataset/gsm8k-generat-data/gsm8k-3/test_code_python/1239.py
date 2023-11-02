def solution():
    """Tom decides to get a new floor for his room.  It cost $50 to remove the floor.  The new floor costs $1.25 per square foot and Tom's room is 8*7 feet.  How much did it cost to replace the floor?"""
    # Define the cost to remove the old floor and the cost per square foot of the new floor
    REMOVAL_COST = 50
    NEW_FLOOR_COST = 1.25

    # Calculate the area of Tom's room
    room_area = 8 * 7

    # Calculate the total cost of the new floor, including the cost to remove the old floor
    total_cost = REMOVAL_COST + NEW_FLOOR_COST * room_area

    # Display the total cost of the new floor
    result = total_cost
    return result

print(solution())