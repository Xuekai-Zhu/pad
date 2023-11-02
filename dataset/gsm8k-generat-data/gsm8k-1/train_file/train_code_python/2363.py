def solution():
    """Ms. Mitsuko told the class that if the average score on their quiz is higher than 75% then they will get a pizza party. There are 25 students in the class. One student is absent and has to take the test the next day. The average score of the students who took the test was 77%. What is the lowest grade the absent student can get for the class to still get a pizza party?"""
    total_students = 25
    target_average = 75
    current_average = 77
    sum_of_scores = current_average * (total_students - 1)
    minimum_score_needed = (target_average * total_students) - sum_of_scores
    result = minimum_score_needed
    return result

print(solution())