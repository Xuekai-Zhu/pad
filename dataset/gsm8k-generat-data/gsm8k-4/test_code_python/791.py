def solution():
    """Of the 90 people on William's bus, 3/5 were Dutch. Of the 1/2 of the Dutch who were also American, 1/3 got window seats. What's the number of Dutch Americans who sat at the windows?"""
    # Define the total number of people on the bus
    total_people = 90

    # Calculate the number of Dutch people on the bus
    dutch_people = total_people * 3/5

    # Calculate the number of Dutch Americans on the bus
    dutch_americans = dutch_people * 1/2

    # Calculate the number of Dutch Americans who got window seats
    dutch_americans_windows = dutch_americans * 1/3

    # Return the result
    result = dutch_americans_windows
    return result

print(solution())