def solution():
    distance = 448  # Distance between New Orleans and Dallas is 448 miles
    time_first_spaceship = 0.5  # The first spaceship took 30 minutes (0.5 hours) to travel to Dallas
    time_second_spaceship = 1  # The second spaceship took 1 hour to travel to Dallas
    speed_first_spaceship = distance / time_first_spaceship  # Calculate the speed of the first spaceship
    speed_second_spaceship = distance / time_second_spaceship  # Calculate the speed of the second spaceship

    # Calculate the difference in speed between the two spaceships
    speed_difference = abs(speed_first_spaceship - speed_second_spaceship)
    result = speed_difference
    return result

print(solution())