def solution():
    """Uncle Lou was given four bags of peanuts to eat on his 2-hour plane flight.  Each bag contains 30 peanuts.  If he eats all of the peanuts during the flight, one at a time, consumed at equally spaced intervals, what is the length of time, in minutes, between eating each peanut?"""
    # Calculate the total number of peanuts
    total_peanuts = 4 * 30

    # Calculate the total time in minutes for the flight
    total_time = 2 * 60

    # Calculate the time between eating each peanut
    time_between_peanuts = total_time / (total_peanuts - 1)

    # Display the time between eating each peanut
    result = time_between_peanuts
    return result

print(solution())