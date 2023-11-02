def solution():
    
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