def solution():
    
    # Define the dimensions of the walls
    north_worth = 10
    east_worth = 5

    # Calculate the total area of the walls
    total_area = north_worth * east_worth

    # Calculate the total area of the room
    room_area = total_area * 4

    # Calculate the number of gallons of paint needed
    gallons_needed = room_area / 20

    # Calculate the total cost of the room
    room_cost = gallons_needed * 12

    # return the result
    result = room_cost
    return result

print(solution())