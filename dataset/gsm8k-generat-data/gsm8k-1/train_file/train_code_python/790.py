def solution():
    """Of the 90 people on William's bus, 3/5 were Dutch. Of the 1/2 of the Dutch who were also American, 1/3 got window seats. What's the number of Dutch Americans who sat at the windows?"""
    total_people = 90
    dutch_ratio = 3/5
    dutch_people = total_people * dutch_ratio
    dutch_american_ratio = 1/2
    dutch_americans = dutch_people * dutch_american_ratio
    window_ratio = 1/3
    dutch_americans_windows = dutch_americans * window_ratio
    result = dutch_americans_windows
    return result

print(solution())