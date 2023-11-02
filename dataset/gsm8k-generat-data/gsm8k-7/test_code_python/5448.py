def solution():
    jim_distance = 16
    jim_time = 2
    frank_distance = 20
    frank_time = 2

    # Calculate Jim's speed in miles per hour
    jim_speed = jim_distance / jim_time

    # Calculate Frank's speed in miles per hour
    frank_speed = frank_distance / frank_time

    # Calculate the difference in their speeds
    speed_difference = frank_speed - jim_speed

    # Calculate how many more miles Frank ran than Jim in an hour
    distance_difference = speed_difference * 1  # They ran for the same amount of time

    result = distance_difference
    return result

print(solution())