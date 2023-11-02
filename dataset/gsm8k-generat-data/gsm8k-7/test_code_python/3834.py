def solution():
    # Each token gets you 15 pitches
    num_pitches_per_token = 15

    # Macy used 11 tokens and hit the ball 50 times
    macy_tokens = 11
    macy_hits = 50

    # Piper used 17 tokens and hit the ball 55 times
    piper_tokens = 17
    piper_hits = 55

    # Calculate the total number of pitches for each player
    macy_total_pitches = macy_tokens * num_pitches_per_token
    piper_total_pitches = piper_tokens * num_pitches_per_token

    # Calculate the number of pitches missed by each player
    macy_missed_pitches = macy_total_pitches - macy_hits
    piper_missed_pitches = piper_total_pitches - piper_hits

    # Calculate the total number of pitches missed by both players
    total_missed_pitches = macy_missed_pitches + piper_missed_pitches

    result = total_missed_pitches
    return result

print(solution())