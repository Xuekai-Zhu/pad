def solution():
    """Jane is dividing up minnows to be carnival prizes. She bought 600 minnows, and each prize is a bowl with 3 minnows.
    If 800 people are going to play the game and 15% win a prize, how many minnows will be left over?"""
    total_minnows = 600
    total_players = 800
    minnows_per_prize = 3
    win_probability = 0.15
    total_prizes = int(total_players * win_probability)
    minnows_needed = total_prizes * minnows_per_prize
    minnows_left = total_minnows - minnows_needed
    result = minnows_left
    return result

print(solution())