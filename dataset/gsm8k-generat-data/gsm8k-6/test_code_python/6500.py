def solution():
    # Calculate the number of matches Sam won in his first 100 matches
    matches_won_100 = 0.5 * 100  # 50% of matches won

    # Calculate the number of matches Sam won in his next 100 matches
    matches_won_200 = 0.6 * 100  # 60% of matches won

    # Calculate the total number of matches Sam won
    total_matches_won = matches_won_100 + matches_won_200

    result = total_matches_won
    return result

print(solution())