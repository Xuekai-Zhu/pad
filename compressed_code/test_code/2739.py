def solution():
    
    total_bottles = 4 * 12
    players = 11
    first_break_bottles = players * 2
    end_game_bottles = players
    remaining_bottles = total_bottles - first_break_bottles - end_game_bottles
    result = remaining_bottles
    return result

print(solution())