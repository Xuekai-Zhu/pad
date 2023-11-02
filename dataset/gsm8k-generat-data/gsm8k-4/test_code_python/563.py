def solution():
    """There are 84 people waiting in line to ride a roller coaster at an amusement park. The roller coaster has 7 cars, and each car seats 2 people. How many times will the ride operator have to run the roller coaster to give everyone in line a turn?"""
    # Calculate the total number of seats on the rollercoaster
    total_seats = 7 * 2

    # Calculate the number of times the rollercoaster needs to be run
    runs = 84 // total_seats
    if 84 % total_seats != 0:
        runs += 1

    # Return the result
    result = runs
    return result

print(solution())