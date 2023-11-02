def solution():
    """Hannah wants to get the highest grade in the class on the upcoming math test. Because she is out sick the day of the test, she learns ahead of time the top scores she has to beat. She finds out that one student got a 95% on the exam. Another student only got 3 wrong out of 40. How many questions does she have to get right to have the highest score in the class?"""
    # To get a higher score than the first student, Hannah needs to get more than 95%.
    # To get a higher score than the second student, Hannah needs to get more than 37 correct out of 40 (93%).
    
    highest_score_percentage = max(95, 93)
    highest_score_questions = int(highest_score_percentage / 100 * 40)
    result = highest_score_questions
    return result

print(solution())