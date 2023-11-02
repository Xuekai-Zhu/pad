def solution():
    layla_score = 104
    kristin_score = layla_score - 24
    total_score = layla_score + kristin_score
    num_games = 4
    avg_score = total_score / (2 * num_games)
    result = avg_score
    return result

print(solution())