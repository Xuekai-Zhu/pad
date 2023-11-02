def solution():
    """Janet starts driving across a lake in a speedboat going 30 miles per hour. Her sister follows in a sailboat that has a speed of 12 miles per hour. If the lake is 60 miles wide, how long does Janet have to wait on the other side for her sister to catch up?"""
    janet_speed = 30
    sister_speed = 12
    distance = 60
    time = distance / (janet_speed - sister_speed)
    result = time
    return result

print(solution())