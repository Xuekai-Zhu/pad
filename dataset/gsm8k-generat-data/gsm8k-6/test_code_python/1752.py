def solution():
    # Calculate Jose's total score
    jose_score = 48 * 2  # Jose got 5 questions wrong, so he scored (50 - 5) * 2 = 90 marks
    # Calculate Meghan's score
    meghan_score = jose_score - 20  # Meghan scored 20 marks less than Jose
    # Calculate Alisson's score
    alisson_score = jose_score - 40  # Jose scored 40 marks more than Alisson
    # Calculate the total score for the three
    total_score = jose_score + meghan_score + alisson_score
    result = total_score
    return result

print(solution())