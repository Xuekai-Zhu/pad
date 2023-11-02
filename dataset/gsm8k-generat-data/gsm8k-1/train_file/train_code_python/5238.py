def solution():
    """Uncle Lou was given four bags of peanuts to eat on his 2-hour plane flight. Each bag contains 30 peanuts. If he eats all of the peanuts during the flight, one at a time, consumed at equally spaced intervals, what is the length of time, in minutes, between eating each peanut?"""
    total_peanuts = 4 * 30
    flight_time = 2 * 60 # convert hours to minutes
    time_between_peanuts = flight_time / total_peanuts
    result = time_between_peanuts
    return result

print(solution())