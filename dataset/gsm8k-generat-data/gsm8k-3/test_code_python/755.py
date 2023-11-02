def solution():
    """Tom swims for 2 hours at a speed of 2 miles per hour.  He then runs for half the time at 4 times the speed.  How many miles did he cover?"""
    # Calculate the distance Tom swims
    swim_distance = 2 * 2 # distance = speed * time

    # Calculate the time Tom runs
    run_time = 2 / 2 # half of the total time

    # Calculate the distance Tom runs
    run_distance = 4 * run_time # distance = speed * time

    # Calculate the total distance Tom covered
    total_distance = swim_distance + run_distance

    # Display the total distance
    result = total_distance
    return result

print(solution())