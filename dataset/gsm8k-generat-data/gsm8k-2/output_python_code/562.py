def solution():
    """There are 84 people waiting in line to ride a roller coaster at an amusement park. The roller coaster has 7 cars, and each car seats 2 people. How many times will the ride operator have to run the roller coaster to give everyone in line a turn?"""
    total_people = 84
    cars = 7
    per_car_capacity = 2
    total_capacity = cars * per_car_capacity
    rides_needed = total_people // total_capacity
    if total_people % total_capacity != 0:
        rides_needed += 1
    result = rides_needed
    return result

print(solution())