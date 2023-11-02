def solution():
    
    roosevelt_first_game = 30
    roosevelt_second_game = roosevelt_first_game / 2
    roosevelt_third_game = roosevelt_second_game * 3
    roosevelt_total_score = roosevelt_first_game + roosevelt_second_game + roosevelt_third_game + 50
    greendale_total_score = roosevelt_total_score - 10
    result = greendale_total_score
    return result

print(solution())