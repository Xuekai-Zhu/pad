def solution():
    """Rachel is stuffing envelopes. She has eight hours to complete the task and there are 1,500 envelopes. In the first hour, Rachel stuffs 135 envelopes. The second hour she stuffs 141 envelopes. How many envelopes will Rachel need to stuff per hour to finish the job?"""
    total_envelopes = 1500
    hours_left = 8 - 2
    envelopes_left = total_envelopes - 135 - 141
    envelopes_per_hour = envelopes_left / hours_left
    result = envelopes_per_hour
    return result

print(solution())