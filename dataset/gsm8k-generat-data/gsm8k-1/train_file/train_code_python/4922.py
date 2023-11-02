def solution():
    """Austin and Jake start descending from the 9th floor of a building at the same time. Austin uses the elevator and Jake uses the stairs, descending 3 steps every second. The stairs have 30 steps across each floor. If the elevator will take a minute to get to ground level, how many seconds later will Jake get to the ground floor?"""
    starting_floor = 9
    steps_per_floor = 30
    total_steps = (starting_floor - 1) * steps_per_floor
    seconds_to_reach_ground = 60
    seconds_to_reach_ground -= 1 #Subtract 1 minute for elevator
    seconds_to_reach_ground -= (total_steps / 3) #Subtract seconds for Jake's descent
    result = seconds_to_reach_ground
    return result

print(solution())