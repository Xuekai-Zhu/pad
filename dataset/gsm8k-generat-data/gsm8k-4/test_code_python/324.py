def solution():
    """A building has four floors with ten rooms each. Legacy has to clean each room, and it takes her 6 hours to clean one room. If she earns $15 per hour of work, calculate the total amount of money she makes from cleaning all the floors in the building."""
    # Define the number of floors and rooms per floor
    num_floors = 4
    rooms_per_floor = 10

    # Define the time it takes to clean one room and the hourly pay rate
    time_per_room = 6
    hourly_pay = 15

    # Calculate the total number of rooms in the building
    total_rooms = num_floors * rooms_per_floor

    # Calculate the total time to clean all the rooms
    total_time = total_rooms * time_per_room

    # Calculate the total earnings for cleaning all the rooms
    total_earnings = total_time * hourly_pay

    # Return the result
    result = total_earnings
    return result

print(solution())