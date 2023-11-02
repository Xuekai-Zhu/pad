def solution():
    
    lefty_score = 20
    righty_score = lefty_score / 2
    third_teammate_score = righty_score * 6
    total_points = lefty_score + righty_score + third_teammate_score
    num_players = 3
    average_score = total_points / num_players
    result = average_score
    return result

print(solution())