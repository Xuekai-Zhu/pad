def solution():
    people_on_bus = 90
    dutch_people = people_on_bus * (3 / 5)
    dutch_americans = dutch_people * (1 / 2)
    dutch_americans_in_window_seats = dutch_americans * (1 / 3)
    
    result = dutch_americans_in_window_seats
    return result

print(solution())