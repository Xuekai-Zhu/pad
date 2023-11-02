def solution():
    chase_speed = 2
    cameron_speed = chase_speed / 2
    danielle_speed = cameron_speed * 3
    time_to_travel = 30
    chase_time_to_travel = time_to_travel / (danielle_speed / chase_speed) 
    result = chase_time_to_travel
    return result

print(solution())