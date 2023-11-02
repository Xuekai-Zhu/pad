def solution():
    """Of the 90 people on William's bus, 3/5 were Dutch. Of the 1/2 of the Dutch who were also American, 1/3 got window seats. What's the number of Dutch Americans who sat at the windows?"""
    total_passengers = 90
    dutch_passengers = (3/5) * total_passengers
    dutch_americans = (1/2) * dutch_passengers
    dutch_americans_window = (1/3) * dutch_americans
    result = dutch_americans_window
    return result

print(solution())