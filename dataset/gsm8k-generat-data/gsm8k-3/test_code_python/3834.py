def solution():
    """Macy and Piper went to the batting cages. Each token gets you 15 pitches.
    Macy used 11 tokens and Piper used 17. Macy hit the ball 50 times. Piper hit the ball 55 times.
    How many pitches did Macy and Piper miss altogether?"""
    
    # Calculate the total number of pitches for Macy and Piper
    macy_pitches = 11 * 15
    piper_pitches = 17 * 15
    
    # Calculate the number of pitches missed by Macy and Piper
    macy_missed = macy_pitches - 50
    piper_missed = piper_pitches - 55
    
    # Calculate the total number of pitches missed
    total_missed = macy_missed + piper_missed
    
    # Return the total number of pitches missed
    return total_missed

print(solution())