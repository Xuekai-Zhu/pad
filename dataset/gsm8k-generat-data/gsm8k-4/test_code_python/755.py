def solution():
    """Tom swims for 2 hours at a speed of 2 miles per hour. He then runs for half the time at 4 times the speed. How many miles did he cover?"""
    # Define the swimming time, swimming speed, running time, and running speed
    swim_time = 2
    swim_speed = 2
    run_time = swim_time / 2
    run_speed = 2 * 4

    # Calculate the distance covered during swimming and running
    swim_distance = swim_time * swim_speed
    run_distance = run_time * run_speed

    # Calculate the total distance covered
    total_distance = swim_distance + run_distance

    # Return the result
    result = total_distance
    return result

print(solution())