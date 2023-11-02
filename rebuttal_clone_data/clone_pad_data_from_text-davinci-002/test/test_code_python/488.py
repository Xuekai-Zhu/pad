def solution():
    actors_per_show = 5
    time_per_actor = 15
    total_time = 60
    total_actors = actors_per_show * (total_time / time_per_actor)
    result = total_actors
    return result

print(solution())