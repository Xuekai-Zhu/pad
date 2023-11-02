def solution():
    """Rachel is stuffing envelopes. She has eight hours to complete the task, and there are 1,500 envelopes. In the first hour, Rachel stuffs 135 envelopes. The second hour she stuffs 141 envelopes. How many envelopes will Rachel need to stuff per hour to finish the job?"""
    # Define the total time and number of envelopes
    total_time = 8
    total_envelopes = 1500

    # Define the number of envelopes stuffed in the first two hours
    envelopes_stuffed = 135 + 141

    # Calculate the number of envelopes left to stuff
    envelopes_left = total_envelopes - envelopes_stuffed

    # Calculate the time left to stuff envelopes
    time_left = total_time - 2

    # Calculate the rate at which Rachel needs to stuff envelopes
    rate = envelopes_left / time_left

    # return the result
    result = round(rate)
    return result

print(solution())