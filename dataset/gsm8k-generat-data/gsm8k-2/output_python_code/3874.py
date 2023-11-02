def solution():
    """Three snails raced across a rain-soaked sidewalk. The first snail raced at a speed of 2 feet per minute. The second snail raced at twice the speed of the first snail. And the third snail traveled at five times the rate of speed as the second snail. If it took the first snail 20 minutes to race all the way up the sidewalk, how long, in minutes, did it take for the third snail to race all the way up the sidewalk?"""
    first_snail_speed = 2
    second_snail_speed = first_snail_speed * 2
    third_snail_speed = second_snail_speed * 5
    distance = 1  # let's assume the distance is 1 unit
    first_snail_time = 20
    third_snail_time = distance / third_snail_speed * 60
    result = third_snail_time
    return result

print(solution())