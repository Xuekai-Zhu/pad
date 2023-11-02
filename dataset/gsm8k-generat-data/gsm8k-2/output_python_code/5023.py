def solution():
    """John trains for ultramarathons. He starts only able to run 8 hours straight but eventually increases that by 75%. He also increases his speed of 8 mph by 4 mph. How far can he run now?"""
    initial_time = 8
    increased_time = initial_time * 1.75
    initial_speed = 8
    increased_speed = initial_speed + 4
    distance = increased_time * increased_speed
    result = distance
    return result

print(solution())