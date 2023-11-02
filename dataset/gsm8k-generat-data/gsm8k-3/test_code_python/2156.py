def solution():
    """Billy can spit a watermelon seed 30 inches.  Madison can spit a watermelon seed 20% farther than Billy.  Ryan can spit a watermelon seed 50% shorter than Madison.  How far can Ryan spit a watermelon seed?"""
    # Define Billy's spit distance
    billy_spit = 30

    # Calculate Madison's spit distance
    madison_spit = billy_spit * 1.2

    # Calculate Ryan's spit distance
    ryan_spit = madison_spit * 0.5

    # Display Ryan's spit distance
    result = ryan_spit
    return result

print(solution())