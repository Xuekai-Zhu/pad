def solution():
    """Jane is dividing up minnows to be carnival prizes. She bought 600 minnows, and each prize is a bowl with 3 minnows. If 800 people are going to play the game and 15% win a prize, how many minnows will be left over?"""
    total_minnows = 600
    minnows_per_prize = 3
    total_prizes = 800 * 0.15
    minnows_used = total_prizes * minnows_per_prize
    minnows_left = total_minnows - minnows_used
    result = minnows_left
    return result

print(solution())