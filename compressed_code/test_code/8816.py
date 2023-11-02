def solution():
    
    macy_tokens = 11
    piper_tokens = 17
    pitches_per_token = 15
    macy_hits = 50
    piper_hits = 55
    macy_misses = (macy_tokens * pitches_per_token) - macy_hits
    piper_misses = (piper_tokens * pitches_per_token) - piper_hits
    total_misses = macy_misses + piper_misses
    result = total_misses
    return result

print(solution())