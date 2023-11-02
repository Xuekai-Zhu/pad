def solution():
    # Collect data on mall Santa actors
    white_actors = 0
    black_actors = 1
    other_actors = 0
    # Determine if most mall Santa actors are white
    if white_actors > black_actors and white_actors > other_actors:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())