def solution():
    snowballs_per_hour = 20  # Jay can build 20 snowballs in an hour
    snowballs_per_melt = 2  # Jay can build 2 melt every 15 minutes
    total_snowballs = 60  # Jay wants to have 60 snowballs

    # Calculate the total time it will take Jay to build all the snowballs
    time_in_minutes = (total_snowballs / snowballs_per_melt) * 60
    result = time_in_minutes
    return result

print(solution())