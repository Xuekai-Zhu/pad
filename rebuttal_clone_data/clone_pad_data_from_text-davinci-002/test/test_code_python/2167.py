def solution():
    total_pitches = 15
    total_tokens = 11 + 17
    total_hits = 50 + 55
    total_misses = total_tokens * total_pitches - total_hits
    result = total_misses
    return result

print(solution())