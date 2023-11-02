def solution():
    # Calculate Tom's score without the bonus
    score_no_bonus = 150 * 10  # 10 points for killing an enemy

    if score_no_bonus >= 1000:  # if Tom kills at least 100 enemies
        # Calculate Tom's bonus score
        bonus = score_no_bonus * 0.5
        total_score = score_no_bonus + bonus
    else:
        total_score = score_no_bonus

    result = total_score
    return result

print(solution())