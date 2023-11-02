def solution():
    """There are 84 people waiting in line to ride a roller coaster at an amusement park. The roller coaster has 7 cars, and each car seats 2 people. How many times will the ride operator have to run the roller coaster to give everyone in line a turn?"""
    # Calculate the total number of seats on the roller coaster
    total_seats = 7 * 2

    # Calculate the number of times the ride operator will have to run the roller coaster
    times_to_run = 84 // total_seats
    if 84 % total_seats != 0:
        times_to_run += 1

    # Display the number of times the ride operator will have to run the roller coaster
    result = times_to_run
    return result

print(solution())