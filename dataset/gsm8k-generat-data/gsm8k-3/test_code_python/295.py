def solution():
    """For every 1 minute that Carlotta sings on stage during the final opera performance, she spends an additional 3 minutes practicing and 5 minutes throwing temper tantrums. If her final stage performance is 6 minutes long, what is the total combined amount of time, in minutes, that she spends practicing, throwing tantrums, and singing in the final stage performance?"""
    # Define the time Carlotta spends practicing, throwing tantrums, and singing for every 1 minute of stage performance
    PRACTICE_TIME = 3
    TANTRUM_TIME = 5

    # Define the length of Carlotta's final stage performance
    STAGE_TIME = 6

    # Calculate the total time Carlotta spends practicing, throwing tantrums, and singing during her final stage performance
    total_time = (PRACTICE_TIME + TANTRUM_TIME + 1) * STAGE_TIME # add 1 minute for singing

    # Display the total time
    result = total_time
    return result

print(solution())