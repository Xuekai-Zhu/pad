def solution():
    """Macy and Piper went to the batting cages. Each token gets you 15 pitches. Macy used 11 tokens and Piper used 17. Macy hit the ball 50 times. Piper hit the ball 55 times. How many pitches did Macy and Piper miss altogether?"""
    # Define the number of tokens used by Macy and Piper
    macy_tokens = 11
    piper_tokens = 17

    # Define the number of pitches in each token
    pitches_per_token = 15

    # Calculate the total number of pitches attempted by Macy and Piper
    macy_pitches = macy_tokens * pitches_per_token
    piper_pitches = piper_tokens * pitches_per_token

    # Calculate the number of pitches missed by Macy and Piper
    macy_missed = macy_pitches - 50
    piper_missed = piper_pitches - 55

    # Calculate the total number of pitches missed
    total_missed = macy_missed + piper_missed

    # return the result
    result = total_missed
    return result

print(solution())