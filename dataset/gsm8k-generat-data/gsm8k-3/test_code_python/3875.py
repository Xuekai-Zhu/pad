def solution():
    """Three snails raced across a rain-soaked sidewalk.  The first snail raced at a speed of 2 feet per minute.  
    The second snail raced at twice the speed of the first snail.  And the third snail traveled at five times the rate of speed as the second snail.  
    If it took the first snail 20 minutes to race all the way up the sidewalk, how long, in minutes, did it take for the third snail to race all the way up the sidewalk?"""
    # Define the speed of the first snail
    speed_1 = 2

    # Define the speed of the second snail
    speed_2 = 2 * speed_1

    # Define the speed of the third snail
    speed_3 = 5 * speed_2

    # Calculate the distance traveled by the first snail
    distance = speed_1 * 20

    # Calculate the time taken by the third snail to travel the same distance
    time_3 = distance / speed_3

    # Return the result
    result = time_3
    return result

print(solution())