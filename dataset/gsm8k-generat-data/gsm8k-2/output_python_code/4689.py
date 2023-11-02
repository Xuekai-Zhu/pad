def solution():
    """Terry drives at a speed of 40 miles per hour. He drives daily forth and back from his home to his workplace which is 60 miles away from his home. How many hours does Terry spend driving from home to the workplace and then back?"""
    distance = 60
    speed = 40
    time_one_way = distance / speed
    total_time = time_one_way * 2
    result = total_time
    return result

print(solution())