def solution():
    initial_running_hours = 8
    percent_increase_hours = 0.75 # 75% increase
    speed_increase_mph = 4

    # Calculate the new number of running hours
    new_running_hours = initial_running_hours * (1 + percent_increase_hours)

    # Calculate the new running speed in mph
    new_running_speed_mph = 8 + speed_increase_mph

    # Calculate the distance that John can run now
    distance = new_running_hours * new_running_speed_mph
    result = distance
    return result

print(solution())