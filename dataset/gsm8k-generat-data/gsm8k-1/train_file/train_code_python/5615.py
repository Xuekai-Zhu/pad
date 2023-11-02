def solution():
    """Xena is trying to outrun a dragon to get to the safety of a cave it's too big to fit into. Xena has a 600 foot head start,
    but the dragon can burn her if it gets within 120 feet of her. If Xena runs 15 feet per second and the dragon flies 30 feet
    per second, how many seconds does Xena have to get to the cave?"""
    
    xena_start = 600
    dragon_start = 0
    xena_speed = 15
    dragon_speed = 30
    dragon_kill_range = 120
    distance_to_cave = 1000
    
    time_to_cave = (distance_to_cave - xena_start) / xena_speed
    time_to_be_killed = (dragon_start + dragon_kill_range - xena_start) / (dragon_speed - xena_speed)
    
    if time_to_cave < time_to_be_killed:
        result = round(time_to_cave, 2)
    else:
        result = "Xena will be burned before she reaches the cave."
        
    return result

print(solution())