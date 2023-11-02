def solution():
    # Calculate James' score for each round
    round_score = 2 * 4 + 4  # 2 points for each correct answer plus 4 point bonus for answering all questions

    # Calculate James' total score for all five rounds
    total_score = round_score * 5  # five rounds

    # Subtract one point for the question James missed
    total_score -= 2

    result = total_score
    return result

print(solution())