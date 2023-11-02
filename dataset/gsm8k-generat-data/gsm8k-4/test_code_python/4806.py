def solution():
    """Melissa is repairing her shoes. For each shoe, it takes her 5 minutes to replace the buckle and 10 minutes to even out the heel. How many minutes does Melissa spend on this project total?"""
    # Define the time it takes to replace a buckle and even out a heel
    BUCKLE_TIME = 5
    HEEL_TIME = 10

    # Define the number of shoes being repaired
    NUM_SHOES = 2

    # Calculate the total time spent on the project
    total_time = NUM_SHOES * (BUCKLE_TIME + HEEL_TIME)

    # Return the result
    result = total_time
    return result

print(solution())