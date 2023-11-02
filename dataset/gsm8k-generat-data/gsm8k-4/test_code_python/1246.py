def solution():
    """A spaceship is traveling to another planet. The spaceship travels at a consistent speed its entire journey unless it is stopped for the crew’s break. After launch, the spaceship traveled for 10 hours then stopped for 3 hours. It then traveled for another 10 hours then stopped for 1 hour. After this, the spaceship would take an hour’s break after every 11 hours of traveling and maintained this routine until the end of its journey. If the entire journey took 3 days then how long, in hours, was the spaceship not moving?"""
    
    # Define the time variables
    total_time = 3 * 24 # in hours
    travel_time = 0
    break_time = 0
    
    # Calculate the travel time for the first two legs of the journey
    travel_time += 10 + 10
    
    # Calculate the break time for the first two stops
    break_time += 3 + 1
    
    # For the remaining journey, calculate the travel time and break time for each cycle of 11 hours of travel
    remaining_time = total_time - 20 # Subtract the time for the first two legs
    while remaining_time > 0:
        if remaining_time >= 11:
            travel_time += 11
            break_time += 1
            remaining_time -= 12 # Subtract the travel time and break time
        else:
            travel_time += remaining_time
            remaining_time = 0
    
    # Calculate the time the spaceship was not moving
    not_moving_time = total_time - travel_time - break_time
    
    # Return the result
    result = not_moving_time
    return result

print(solution())