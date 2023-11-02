def solution():
    total_distance = 10
    speed1 = 3
    time1 = 2
    speed2 = 1

    # Calculate the distance that Diana can bike at her first speed
    distance1 = speed1 * time1

    # Calculate the remaining distance that Diana needs to bike
    remaining_distance = total_distance - distance1

    # Calculate the time it will take Diana to bike the remaining distance at her second speed
    time2 = remaining_distance / speed2

    # Calculate the total time it will take Diana to get home
    total_time = time1 + time2
    result = total_time
    return result

print(solution())