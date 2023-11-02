def solution():
    """Three snails raced across a rain-soaked sidewalk. The first snail raced at a speed of 2 feet per minute. The second snail raced at twice the speed of the first snail. And the third snail traveled at five times the rate of speed as the second snail. If it took the first snail 20 minutes to race all the way up the sidewalk, how long, in minutes, did it take for the third snail to race all the way up the sidewalk?"""
    # Define the speed of each snail in feet per minute
    snail1_speed = 2
    snail2_speed = snail1_speed * 2
    snail3_speed = snail2_speed * 5

    # Calculate the distance each snail traveled in feet
    distance = 20 * 2 * 60  # convert 20 minutes to seconds and multiply by speed

    snail1_distance = distance
    snail2_distance = distance
    snail3_distance = distance

    # Calculate the time it took each snail to travel the distance
    snail1_time = distance / snail1_speed
    snail2_time = distance / snail2_speed
    snail3_time = distance / snail3_speed

    # Return the time taken by the third snail in minutes
    result = snail3_time / 60
    return result

print(solution())