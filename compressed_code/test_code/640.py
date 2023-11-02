def solution():
    
    total_time = 60
    actors_per_cycle = 5
    cycle_time = 15
    total_actors = 0
    while total_time > 0:
        total_actors += actors_per_cycle
        total_time -= cycle_time
    result = total_actors
    return result

print(solution())