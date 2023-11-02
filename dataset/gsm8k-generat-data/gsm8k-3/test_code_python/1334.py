def solution():
    """Rachel is stuffing envelopes. She has eight hours to complete the task, and there are 1,500 envelopes. In the first hour, Rachel stuffs 135 envelopes. The second hour she stuffs 141 envelopes. How many envelopes will Rachel need to stuff per hour to finish the job?"""
    # Define the total number of hours Rachel has to complete the task
    TOTAL_HOURS = 8

    # Define the total number of envelopes that need to be stuffed
    TOTAL_ENVELOPES = 1500

    # Calculate the number of envelopes that Rachel has already stuffed
    already_stuffed = 135 + 141

    # Calculate the number of envelopes that Rachel has left to stuff
    left_to_stuff = TOTAL_ENVELOPES - already_stuffed

    # Calculate the number of hours Rachel has left to complete the task
    hours_left = TOTAL_HOURS - 2

    # Calculate the number of envelopes Rachel needs to stuff per hour to finish the job on time
    per_hour = left_to_stuff / hours_left

    # Display the number of envelopes Rachel needs to stuff per hour
    result = per_hour
    return result

print(solution())