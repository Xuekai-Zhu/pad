def solution():
    time_left = 8 - 2  # Rachel has used 2 hours already
    envelopes_left = 1500 - 135 - 141  # Rachel has stuffed 135 + 141 envelopes already
    envelopes_per_hour = envelopes_left / time_left
    result = envelopes_per_hour
    return result

print(solution())