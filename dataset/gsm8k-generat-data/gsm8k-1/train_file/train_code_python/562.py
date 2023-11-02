def solution():
    """There are 84 people waiting in line to ride a roller coaster at an amusement park. The roller coaster has 7 cars, and each car seats 2 people. How many times will the ride operator have to run the roller coaster to give everyone in line a turn?"""
    people_in_line = 84
    seats_per_car = 2
    cars_needed = people_in_line // seats_per_car
    if people_in_line % seats_per_car != 0:
        cars_needed += 1
        
    result = cars_needed
    
    return result

print(solution())