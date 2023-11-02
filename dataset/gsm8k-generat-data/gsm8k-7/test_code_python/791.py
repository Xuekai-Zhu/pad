def solution():
    total_people = 90
    dutch_fraction = 3/5
    dutch_people = dutch_fraction * total_people
    dutch_american_fraction = 1/2
    dutch_american = dutch_american_fraction * dutch_people
    window_fraction = 1/3
    dutch_americans_at_window = window_fraction * dutch_american
    result = dutch_americans_at_window
    return result

print(solution())