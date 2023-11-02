def solution():
    """Ms. Mitsuko told the class that if the average score on their quiz is higher than 75% then they will get a pizza party. There are 25 students in the class. One student is absent and has to take the test the next day. The average score of the students who took the test was 77%. What is the lowest grade the absent student can get for the class to still get a pizza party?"""
    # Define the total number of students and the target average score
    total_students = 25
    target_average = 75

    # Calculate the sum of scores for the students who took the test and the sum of scores for the entire class
    sum_scores = 77 * (total_students - 1)
    sum_class = target_average * total_students

    # Calculate the minimum score required for the absent student to still achieve the target average
    min_score = sum_class - sum_scores

    result = min_score
    return result

print(solution())