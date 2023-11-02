def solution():
    
    total_envelopes = 1500
    hours_left = 6
    envelopes_left = total_envelopes - (135 + 141)
    envelopes_per_hour = envelopes_left / hours_left
    result = envelopes_per_hour
    return result

print(solution())