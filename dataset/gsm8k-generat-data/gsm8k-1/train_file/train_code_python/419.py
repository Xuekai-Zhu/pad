def solution():
    """Miriam spent 30 minutes doing laundry, 15 minutes cleaning the bathroom, a certain amount of time cleaning her room, and 40 minutes doing homework. If she spent a total of two hours on these tasks, how long, in minutes, did she spend cleaning her room?"""
    total_time = 2 * 60  # convert to minutes
    laundry_time = 30
    bathroom_time = 15
    homework_time = 40
    room_time = total_time - laundry_time - bathroom_time - homework_time
    result = room_time
    return result

print(solution())