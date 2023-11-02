def solution():
    
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