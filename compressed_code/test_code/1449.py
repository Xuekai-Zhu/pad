def solution():
    
    edmonton_to_red_deer = 220
    red_deer_to_calgary = 110
    total_distance = edmonton_to_red_deer + red_deer_to_calgary
    speed = 110
    time = total_distance / speed
    result = time
    return result

print(solution())