def solution():
    # Define the monkey's swing and run speeds
    swing_speed = 10
    run_speed = 15

    # Calculate the distance traveled during the run
    run_distance = run_speed * 5

    # Calculate the distance traveled during the swing
    swing_distance = swing_speed * 10

    # Calculate the total distance traveled
    total_distance = run_distance + swing_distance
    result = total_distance
    return result

print(solution())