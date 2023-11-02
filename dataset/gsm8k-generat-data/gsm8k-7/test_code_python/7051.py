def solution():
    num_minnows = 600
    num_players = 800
    win_percentage = 0.15
    num_prizes = num_players * win_percentage
    num_minnows_per_prize = 3
    total_minnows_for_prizes = num_prizes * num_minnows_per_prize
    num_minnows_left = num_minnows - total_minnows_for_prizes
    result = num_minnows_left
    return result

print(solution())