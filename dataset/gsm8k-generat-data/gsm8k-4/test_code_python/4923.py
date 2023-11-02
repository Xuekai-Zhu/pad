def solution():
    """Austin and Jake start descending from the 9th floor of a building at the same time. Austin uses the elevator and Jake uses the stairs, descending 3 steps every second. The stairs have 30 steps across each floor. If the elevator will take a minute to get to ground level, how many seconds later will Jake get to the ground floor?"""
    
    # Define the number of floors
    num_floors = 9
    
    # Define the number of steps per floor
    steps_per_floor = 30
    
    # Define the total number of steps for Jake
    total_steps = num_floors * steps_per_floor
    
    # Define the time it takes for Austin to reach the ground floor in seconds
    austin_time = 60
    
    # Define the time it takes for Jake to reach the ground floor in seconds
    jake_time = total_steps / 3
    
    # Subtract Austin's time from Jake's time to get the time difference
    time_difference = jake_time - austin_time
    
    result = time_difference
    return result

print(solution())