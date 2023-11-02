def solution():
    """Edmonton is 220 kilometers north of Red Deer. Calgary is 110 kilometers south of Red Deer. If you travel at 110 kilometers per hour, how long will it take to get from Edmonton to Calgary?"""
    edmonton_to_red_deer = 220
    red_deer_to_calgary = 110
    total_distance = edmonton_to_red_deer + red_deer_to_calgary
    speed = 110
    time = total_distance / speed
    result = time
    return result

print(solution())