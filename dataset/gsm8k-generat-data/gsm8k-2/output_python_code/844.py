def solution():
    """In a show, there can be 5 actors at a time. Every actor is in the show for about 15 minutes, and then another 5 actors come in. How many actors can there be on the show in 1 hour?"""
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