def solution():
    """
    A spaceship is traveling to another planet. The spaceship travels at a consistent speed its entire journey unless 
    it is stopped for the crew’s break. After launch, the spaceship traveled for 10 hours then stopped for 3 hours. 
    It then traveled for another 10 hours then stopped for 1 hour. After this, the spaceship would take an hour’s 
    break after every 11 hours of traveling and maintained this routine until the end of its journey. 
    If the entire journey took 3 days then how long, in hours, was the spaceship not moving?
    """
    launch_time = 0
    first_break_time = 10 + 3
    second_break_time = first_break_time + 10 + 1
    total_break_time = 3 + 1
    
    # calculate total travel time excluding breaks
    total_travel_time = (72 - total_break_time) * 11
    
    # calculate total time spaceship was launched
    total_launch_time = launch_time + first_break_time + second_break_time + total_travel_time
    
    # calculate total time spaceship was not moving
    total_breaks = (3 * 24) // 12  # 3 days with a break every 12 hours
    total_break_time = total_breaks * total_break_time
    
    result = total_break_time
    return result

print(solution())