def solution():
    """Edmonton is 220 kilometers north of Red Deer. Calgary is 110 kilometers south of Red Deer. If you travel at 110 kilometers per hour, how long will it take to get from Edmonton to Calgary?"""
    distance_between_cities = 220 + 110
    speed = 110
    time = distance_between_cities / speed
    result = time
    return result

print(solution())