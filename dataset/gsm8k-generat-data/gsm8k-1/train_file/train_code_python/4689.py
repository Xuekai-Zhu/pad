def solution():
    """Terry drives at a speed of 40 miles per hour. He drives daily forth and back from his home to his workplace which is 60 miles away from his home. How many hours does Terry spend driving from home to the workplace and then back?"""
    speed = 40
    distance = 60
    time = (distance * 2) / speed
    result = time
    return result

print(solution())