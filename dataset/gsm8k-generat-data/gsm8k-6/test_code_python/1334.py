def solution():
    # Calculate the total number of envelopes Rachel needs to stuff
    total_envelopes = 1500
    envelopes_left = total_envelopes - 135 - 141  # envelopes left after first 2 hours

    # Calculate the number of envelopes Rachel needs to stuff per hour to finish the job
    time_left = 8 - 2  # hours left after first 2 hours
    envelopes_per_hour = envelopes_left / time_left
    result = envelopes_per_hour
    return result

print(solution())