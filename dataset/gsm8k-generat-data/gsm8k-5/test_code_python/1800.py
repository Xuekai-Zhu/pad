def solution():
    leo_mistakes = 4  # Half the number of Madeline's mistakes
    brent_mistakes = 5  # One more mistake than Leo
    total_questions = 25  # Total number of questions in the exam

    # Calculate the number of correct answers for each student
    madeline_correct = (total_questions - 2) / 2
    leo_correct = (total_questions - leo_mistakes)
    brent_correct = (total_questions - brent_mistakes)

    # Calculate the scores of each student
    madeline_score = madeline_correct / total_questions * 100
    leo_score = leo_correct / total_questions * 100
    brent_score = brent_correct / total_questions * 100

    result = madeline_score
    return result

print(solution())