def solution():
    """Billy can spit a watermelon seed 30 inches. Madison can spit a watermelon seed 20% farther than Billy. Ryan can spit a watermelon seed 50% shorter than Madison. How far can Ryan spit a watermelon seed?"""
    billy_distance = 30
    madison_distance = billy_distance * 1.2
    ryan_distance = madison_distance * 0.5
    result = ryan_distance
    return result

print(solution())