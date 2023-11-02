def solution():
    """Austin and Jake start descending from the 9th floor of a building at the same time. Austin uses the elevator and Jake uses the stairs, descending 3 steps every second. The stairs have 30 steps across each floor. If the elevator will take a minute to get to ground level, how many seconds later will Jake get to the ground floor?"""
    total_floors = 9
    steps_per_floor = 30
    total_steps = total_floors * steps_per_floor
    jake_speed = 3
    jake_time = total_steps / jake_speed
    elevator_time = 60
    time_difference = jake_time - elevator_time
    result = time_difference
    return result

print(solution())