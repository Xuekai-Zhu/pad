def solution():
    # Calculate the distance traveled by the first snail in 20 minutes
    distance_first_snail = 2 * 20  # Speed of 2 feet per minute, for 20 minutes

    # Calculate the speed of the second snail
    speed_second_snail = 2 * 2  # Twice the speed of the first snail

    # Calculate the speed of the third snail
    speed_third_snail = 5 * speed_second_snail  # Five times the speed of the second snail

    # Calculate the time taken by the third snail to travel the distance
    time_third_snail = distance_first_snail / speed_third_snail
    result = time_third_snail * 60  # Convert to minutes
    return result

print(solution())