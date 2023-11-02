def solution():
    # Calculate total number of pitches per token
    pitches_per_token = 15

    # Calculate total number of pitches taken by Macy and Piper
    macy_pitches = 11 * pitches_per_token
    piper_pitches = 17 * pitches_per_token

    # Calculate total number of missed pitches by Macy and Piper
    macy_missed = macy_pitches - 50
    piper_missed = piper_pitches - 55

    # Calculate total number of missed pitches altogether
    missed_pitches = macy_missed + piper_missed
    result = missed_pitches
    return result

print(solution())