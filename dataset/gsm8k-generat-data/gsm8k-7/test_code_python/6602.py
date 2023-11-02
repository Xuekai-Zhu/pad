def solution():
    riley_mistakes = 3
    ofelia_score = (35 - riley_mistakes) / 2 + 5
    team_score = 35 - riley_mistakes - ofelia_score
    team_mistakes = team_score
    result = team_mistakes
    return result

print(solution())