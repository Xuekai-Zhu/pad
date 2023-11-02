def solution():
    # Calculate the number of pitches missed by Macy and Piper
    macy_missed = (11*15) - 50  # Macy used 11 tokens and hit the ball 50 times; each token gets you 15 pitches
    piper_missed = (17*15) - 55  # Piper used 17 tokens and hit the ball 55 times; each token gets you 15 pitches
    total_missed = macy_missed + piper_missed
    result = total_missed
    return result

print(solution())