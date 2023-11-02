def solution():
    """A building has 10 floors. It takes 15 seconds to go up the stairs to the even-numbered floors and 9 seconds to go up to the odd-numbered floors. This includes getting to the first floor. How many minutes does it take to get to the 10th floor?"""
    # Define the number of floors and the time taken to climb each floor
    NUM_FLOORS = 10
    EVEN_FLOOR_TIME = 15
    ODD_FLOOR_TIME = 9

    # Initialize the total time taken to climb the building
    total_time = 0

    # Iterate through each floor and add the time taken to climb it
    for floor in range(1, NUM_FLOORS+1):
        if floor % 2 == 0:
            total_time += EVEN_FLOOR_TIME
        else:
            total_time += ODD_FLOOR_TIME
    
    # Convert the total time to minutes
    total_time_minutes = total_time / 60
    
    # Return the result
    result = total_time_minutes
    return result

print(solution())