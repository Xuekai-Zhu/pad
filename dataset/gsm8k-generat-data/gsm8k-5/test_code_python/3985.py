def solution():
    lefty_score = 20
    righty_score = lefty_score / 2
    other_teammate_score = 6 * righty_score
    total_score = lefty_score + righty_score + other_teammate_score
    number_of_players = 3
    average_score_per_player = total_score / number_of_players
    result = average_score_per_player
    return result

print(solution())