def solution():
    """Karen's students are about to take a standardized test. Karen gets a $500 bonus if their average score is above 75, plus an extra $10 bonus for every additional point the average score increases above 75. So far, Karen has graded 8 tests, and the average is 70. Given that each student can have a maximum score of 150, what combined score do the last two tests need to have for Karen to earn a $600 bonus?"""
    total_bonus_needed = 600
    bonus_for_above_75 = 500
    additional_bonus_per_point = 10
    num_students = 8
    max_score_per_student = 150
    current_avg = 70
    total_score_so_far = num_students * current_avg
    total_score_needed = total_score_so_far + ((total_bonus_needed - bonus_for_above_75) / additional_bonus_per_point)
    max_total_score = num_students * max_score_per_student
    score_needed_on_last_two = total_score_needed - total_score_so_far
    score_possible_on_last_two = 2 * max_score_per_student
    result = score_needed_on_last_two - score_possible_on_last_two
    return result

print(solution())