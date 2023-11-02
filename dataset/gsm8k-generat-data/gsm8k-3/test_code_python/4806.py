def solution():
    """Melissa is repairing her shoes. For each shoe, it takes her 5 minutes to replace the buckle and 10 minutes to even out the heel. How many minutes does Melissa spend on this project total?"""
    # Define the time it takes to replace a buckle and even out a heel
    BUCKLE_TIME = 5
    HEEL_TIME = 10

    # Define the number of shoes that need repaired
    num_shoes = 2

    # Calculate the total time spent on the project
    total_time = (BUCKLE_TIME + HEEL_TIME) * num_shoes

    # Display the total time spent
    result = total_time
    return result

print(solution())