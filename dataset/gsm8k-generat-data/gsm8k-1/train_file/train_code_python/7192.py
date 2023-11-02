def solution():
    """Hannah wants to get the highest grade in the class on the upcoming math test. Because she is out sick the day of the test, she learns ahead of time the top scores she has to beat. She finds out that one student got a 95% on the exam. Another student only got 3 wrong out of 40. How many questions does she have to get right to have the highest score in the class?"""
    max_score = 100
    score_1 = 95
    score_2 = (40 - 3) / 40 * 100
    highest_score_to_beat = max(score_1, score_2)
    questions_correct = int(highest_score_to_beat / 100 * 50)
    result = questions_correct
    return result

print(solution())