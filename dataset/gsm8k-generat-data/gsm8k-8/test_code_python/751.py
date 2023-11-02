def solution():
    # Define the distance Harry ran on Monday
    monday_distance = 10

    # Calculate the distance Harry ran from Tuesday to Thursday
    tues_thurs_distance = 1.5 * monday_distance

    # Calculate Harry's speed on Friday
    friday_speed = 1.6 * tues_thurs_distance

    result = friday_speed
    return result

print(solution())