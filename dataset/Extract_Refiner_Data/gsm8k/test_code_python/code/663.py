def solution():
    
    quarter_length = 12
    num_quarters = 4
    total_game_length = quarter_length * num_quarters
    game_length_in_last_quarter = 5
    game_length_last_quarter = total_game_length + game_length_in_last_quarter
    result = game_length_last_quarter
    return result

print(solution())