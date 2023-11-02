def solution():
    """Karen's students are about to take a standardized test. Karen gets a $500 bonus if their average score is above 75, plus an extra $10 bonus for every additional point the average score increases above 75. So far, Karen has graded 8 tests, and the average is 70. Given that each student can have a maximum score of 150, what combined score do the last two tests need to have for Karen to earn a $600 bonus?"""
    total_students = 10
    current_total_score = 8 * 70
    minimum_bonus_score = (75 * total_students) - current_total_score + 500
    additional_bonus = 60
    combined_score_needed = (minimum_bonus_score + additional_bonus) / 2
    result = combined_score_needed
    return result

print(solution())