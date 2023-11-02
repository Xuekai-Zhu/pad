def solution():
    total_distance = 10  # Diana needs to bike 10 miles to get home
    first_leg_time = 2  # Diana can bike for 2 hours at 3 mph
    second_leg_speed = 1  # Diana bikes at 1 mph for the second leg
    second_leg_distance = total_distance - (3 * first_leg_time)  # Calculate the remaining distance

    # Calculate the time it takes for Diana to complete the second leg
    second_leg_time = second_leg_distance / second_leg_speed

    # Total time it takes for Diana to get home
    total_time = first_leg_time + second_leg_time
    result = total_time
    return result

print(solution())