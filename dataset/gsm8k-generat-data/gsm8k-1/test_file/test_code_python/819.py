def solution():
    """Sasha and Julie are best friends playing on opposing basketball teams. The teams have two practice games scheduled. In the first game, Sasha had the home court advantage and scored 14 points. Julie scored 4 fewer points than Sasha in the same game. Sasha always struggles during away games and their second match was at Julie's home court. Sasha scored 6 fewer points in the second game than Julie's score in the first game. How many total points did Sasha score during both games?"""
    sasha_game1_score = 14
    julie_game1_score = sasha_game1_score - 4
    julie_game2_score = sasha_game1_score
    sasha_game2_score = julie_game1_score - 6
    total_score = sasha_game1_score + sasha_game2_score
    result = total_score
    return result

print(solution())