def solution():
    # Calculate the distance each snail traveled up the sidewalk
    distance_first_snail = 2 * 20 / 12 # the snail traveled at a speed of 2 feet per minute and 20 minutes is converted to hours
    distance_second_snail = 2 * distance_first_snail # the second snail traveled at twice the speed of the first snail
    distance_third_snail = 5 * distance_second_snail # the third snail traveled at five times the rate of speed as the second snail

    # Calculate the time each snail took to race all the way up the sidewalk
    time_first_snail = 20  # given in the question
    time_second_snail = distance_second_snail / (2 * 20 / 60) # distance = speed * time, 20 minutes is converted to hours
    time_third_snail = distance_third_snail / (2 * 20 / 60) # distance = speed * time, 20 minutes is converted to hours

    result = time_third_snail
    return result

print(solution())