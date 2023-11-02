def solution():
    
    mary_speed = 10
    jess_speed = 7
    christina_speed = 4
    christina_start_time = 15
    total_time = 30
    total_balloons = 0
    mary_balloons = mary_speed * total_time
    jess_balloons = jess_speed * total_time
    christina_balloons = (total_time - christina_start_time) * christina_speed
    total_balloons = mary_balloons + jess_balloons + christina_balloons
    result = total_balloons
    return result

print(solution())