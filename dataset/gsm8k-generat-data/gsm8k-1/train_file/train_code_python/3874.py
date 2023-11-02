def solution():
    """Three snails raced across a rain-soaked sidewalk. The first snail raced at a speed of 2 feet per minute. The second snail raced at twice the speed of the first snail. And the third snail traveled at five times the rate of speed as the second snail. If it took the first snail 20 minutes to race all the way up the sidewalk, how long, in minutes, did it take for the third snail to race all the way up the sidewalk?"""
    speed_snail_1 = 2
    speed_snail_2 = speed_snail_1 * 2
    speed_snail_3 = speed_snail_2 * 5
    time_snail_1 = 20
    distance_snail = 1  # Assume the distance the snails raced is 1, doesn't affect solution
    time_snail_3 = distance_snail / speed_snail_3 * 60  # Convert to minutes
    result = time_snail_3
    return result

print(solution())