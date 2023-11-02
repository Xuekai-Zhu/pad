def solution():
    distance = 12  # Jeannie hikes 12 miles to Mount Overlook
    speed_out = 4  # Jeannie hikes at a pace of 4 miles per hour on the way out
    speed_back = 6  # Jeannie hikes at a pace of 6 miles per hour on the way back

    # Calculate the time it takes Jeannie to hike to Mount Overlook
    time_out = distance / speed_out

    # Calculate the time it takes Jeannie to hike back from Mount Overlook
    time_back = distance / speed_back

    # Calculate the total time of Jeannie's hike
    total_time = time_out + time_back
    result = total_time
    return result

print(solution())