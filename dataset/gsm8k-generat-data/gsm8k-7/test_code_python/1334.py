def solution():
    total_hours = 8
    total_envelopes = 1500
    envelopes_stuffed_hour1 = 135
    envelopes_stuffed_hour2 = 141

    # Calculate the total number of envelopes stuffed in the first 2 hours
    total_envelopes_stuffed_hour1and2 = envelopes_stuffed_hour1 + envelopes_stuffed_hour2

    # Calculate the number of remaining envelopes after the first 2 hours
    remaining_envelopes = total_envelopes - total_envelopes_stuffed_hour1and2

    # Calculate the number of envelopes that Rachel needs to stuff per hour to finish the job
    envelopes_per_hour = remaining_envelopes / (total_hours - 2)
    result = envelopes_per_hour
    return result

print(solution())