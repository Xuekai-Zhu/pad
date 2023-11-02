def solution():
    """Of the 90 people on William's bus, 3/5 were Dutch. Of the 1/2 of the Dutch who were also American,
    1/3 got window seats. What's the number of Dutch Americans who sat at the windows?"""
    
    # Calculate the number of Dutch people on the bus
    dutch_people = 90 * 3/5
    
    # Calculate the number of Dutch Americans on the bus
    dutch_americans = dutch_people * 1/2
    
    # Calculate the number of Dutch Americans who got window seats
    window_seats = dutch_americans * 1/3
    
    # Display the number of Dutch Americans who sat at the windows
    result = window_seats
    return result

print(solution())