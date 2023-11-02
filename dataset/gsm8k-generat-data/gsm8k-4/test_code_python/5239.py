def solution():
    """Uncle Lou was given four bags of peanuts to eat on his 2-hour plane flight. Each bag contains 30 peanuts. If he eats all of the peanuts during the flight, one at a time, consumed at equally spaced intervals, what is the length of time, in minutes, between eating each peanut?"""
    # Define the total number of peanuts 
    peanuts = 4 * 30
    
    # Define the duration of the plane flight in minutes 
    duration = 2 * 60
    
    # Calculate the time interval between eating each peanut 
    interval = duration / peanuts
    
    # Return the result 
    return interval

print(solution())