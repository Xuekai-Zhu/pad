def solution():
    total_time = 8
    total_envelopes = 1500
    envelopes_stuffed_in_first_two_hours = 135 + 141
    remaining_envelopes = total_envelopes - envelopes_stuffed_in_first_two_hours
    remaining_time = total_time - 2

    envelopes_per_hour = remaining_envelopes / remaining_time
    result = envelopes_per_hour
    return result

print(solution())