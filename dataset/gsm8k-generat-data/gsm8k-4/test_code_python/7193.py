def solution():
    """Hannah wants to get the highest grade in the class on the upcoming math test. Because she is out sick the day of the test, she learns ahead of time the top scores she has to beat. She finds out that one student got a 95% on the exam. Another student only got 3 wrong out of 40. How many questions does she have to get right to have the highest score in the class?"""
    # Calculate the maximum possible score
    max_score = 40

    # Calculate the score of the first student
    first_student_score = 0.95 * max_score

    # Calculate the score of the second student
    second_student_score = (max_score - 3) / max_score

    # Find the highest score
    highest_score = max(first_student_score, second_student_score)

    # Calculate the number of questions Hannah needs to get right to beat the highest score
    questions_to_get_right = round(highest_score * max_score)

    # Display the result
    result = questions_to_get_right
    return result

print(solution())