def solution():
    """For every 1 minute that Carlotta sings on stage during the final opera performance, she spends an additional 3 minutes practicing and 5 minutes throwing temper tantrums. If her final stage performance is 6 minutes long, what is the total combined amount of time, in minutes, that she spends practicing, throwing tantrums, and singing in the final stage performance?"""
    # Define the time spent singing, practicing, and throwing tantrums per minute
    SINGING_MINUTES = 1
    PRACTICING_MINUTES = 3
    TANTRUM_MINUTES = 5

    # Define the length of the final stage performance
    FINAL_PERFORMANCE_MINUTES = 6

    # Calculate the total time spent singing, practicing, and throwing tantrums
    singing_time = SINGING_MINUTES * FINAL_PERFORMANCE_MINUTES
    practicing_time = PRACTICING_MINUTES * FINAL_PERFORMANCE_MINUTES
    tantrum_time = TANTRUM_MINUTES * FINAL_PERFORMANCE_MINUTES

    # Calculate the total combined amount of time
    total_time = singing_time + practicing_time + tantrum_time

    # Return the result
    result = total_time
    return result

print(solution())