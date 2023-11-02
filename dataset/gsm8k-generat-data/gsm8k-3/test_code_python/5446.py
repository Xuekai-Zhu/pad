def solution():
    """A building has 10 floors. It takes 15 seconds to go up the stairs to the even-numbered floors and 9 seconds to go up to the odd-numbered floors.  This includes getting to the first floor. How many minutes does it take to get to the 10th floor?"""
    # Define the time it takes to go up each type of floor
    EVEN_TIME = 15
    ODD_TIME = 9

    # Define the number of floors in the building
    NUM_FLOORS = 10

    # Calculate the total time it takes to get to the 10th floor
    total_time = 0
    for floor in range(1, 11):
        if floor % 2 == 0:
            total_time += EVEN_TIME
        else:
            total_time += ODD_TIME

    # Convert the total time to minutes and display it
    result = total_time / 60
    return result

print(solution())