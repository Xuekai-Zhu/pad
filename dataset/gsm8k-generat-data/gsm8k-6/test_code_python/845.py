def solution():
    # Calculate the number of groups of 5 actors in 1 hour
    groups = 60 // 15  # there are 4 groups of 15 minutes in 1 hour
    # Calculate the total number of actors in 1 hour
    total_actors = groups * 5  # 5 actors come in every 15 minutes
    result = total_actors
    return result

print(solution())