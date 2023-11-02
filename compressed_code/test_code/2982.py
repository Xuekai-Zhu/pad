def solution():
    
    macy_tokens = 11
    piper_tokens = 17
    pitches_per_token = 15
    macy_hits = 50
    piper_hits = 55
    macy_missed = (macy_tokens * pitches_per_token) - macy_hits
    piper_missed = (piper_tokens * pitches_per_token) - piper_hits
    total_missed = macy_missed + piper_missed
    result = total_missed
    return result

print(solution())