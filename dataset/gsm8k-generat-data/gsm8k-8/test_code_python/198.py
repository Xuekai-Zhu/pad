def solution():
    # Convert Tuesday and Thursday's times to hours
    tuesday_hours = 0.5
    thursday_hours = 0.33

    # Calculate the total hours Rosie has already run
    total_hours = 1 + tuesday_hours + 1 + thursday_hours

    # Calculate the distance Rosie has left to run for the week
    distance_left = 20 - (total_hours * 6)

    # Calculate how many minutes Rosie needs to run on Friday to reach her goal
    minutes_to_run = (distance_left / 6) * 60

    result = minutes_to_run
    return result

print(solution())