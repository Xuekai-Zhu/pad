def solution():
    """A building has four floors with ten rooms each. Legacy has to clean each room, and it takes her 6 hours to clean one room. If she earns $15 per hour of work, calculate the total amount of money she makes from cleaning all the floors in the building."""
    # Define the number of floors and rooms per floor
    NUM_FLOORS = 4
    ROOMS_PER_FLOOR = 10

    # Define Legacy's hourly wage and the time it takes to clean one room
    HOURLY_WAGE = 15
    CLEANING_TIME = 6

    # Calculate the total number of rooms to be cleaned
    total_rooms = NUM_FLOORS * ROOMS_PER_FLOOR

    # Calculate the total cleaning time for all the rooms
    total_time = total_rooms * CLEANING_TIME

    # Calculate the total amount of money Legacy earns
    total_earnings = total_time * HOURLY_WAGE

    # Display the total earnings
    result = total_earnings
    return result

print(solution())