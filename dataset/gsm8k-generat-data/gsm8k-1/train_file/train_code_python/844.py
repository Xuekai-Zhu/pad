def solution():
    """In a show, there can be 5 actors at a time. Every actor is in the show for about 15 minutes, and then another 5 actors come in. How many actors can there be on the show in 1 hour?"""
    actors_per_cycle = 5
    cycle_length_minutes = 15
    minutes_per_hour = 60
    cycles_per_hour = (minutes_per_hour // cycle_length_minutes)
    actors_per_hour = actors_per_cycle * cycles_per_hour
    result = actors_per_hour
    return result

print(solution())