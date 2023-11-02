def solution():
    # Calculate the total number of pitches for Macy and Piper
    macy_total_pitches = 11 * 15
    piper_total_pitches = 17 * 15

    # Calculate the number of pitches that Macy and Piper hit
    macy_hits = 50
    piper_hits = 55

    # Calculate the number of pitches that Macy and Piper missed
    macy_misses = macy_total_pitches - macy_hits
    piper_misses = piper_total_pitches - piper_hits

    # Calculate the total number of misses for Macy and Piper
    total_misses = macy_misses + piper_misses
    result = total_misses
    return result

print(solution())