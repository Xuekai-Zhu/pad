def solution():
    """Jimmy needs to score at least 50 points to pass to the next class. He earned 20 points for each of the 3 exams he wrote but lost 5 points during the school year for bad behavior. How many more points can Jimmy lose and still be able to pass the next class?"""
    # Define the passing score and the score Jimmy earned
    PASSING_SCORE = 50
    exam_score = 20 * 3
    behavior_score = -5

    # Calculate the minimum score Jimmy needs to pass
    minimum_score = PASSING_SCORE - exam_score - behavior_score

    # return the result
    result = minimum_score
    return result

print(solution())