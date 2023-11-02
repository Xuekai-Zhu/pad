def solution():
    # Calculate the time it takes Diana to bike 6 miles at 3 mph
    time_at_3mph = 6 / 3  # distance divided by speed

    # Calculate the remaining distance to bike
    remaining_distance = 10 - 6

    # Calculate the time it takes Diana to bike the remaining distance at 1 mph
    time_at_1mph = remaining_distance / 1

    # Calculate the total time it takes Diana to get home
    total_time = time_at_3mph + 2 + time_at_1mph  # Diana bikes for 2 hours at 3 mph before getting tired

    result = total_time
    return result

print(solution())