def solution():
    
    gather_time = 6
    create_time = 9
    total_time = gather_time + create_time
    batteries_per_hour = 60 / total_time
    robots = 10
    total_batteries = batteries_per_hour * 5 * robots
    result = total_batteries
    return result

print(solution())