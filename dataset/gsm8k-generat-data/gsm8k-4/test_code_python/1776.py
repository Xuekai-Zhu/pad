def solution():
    """The teacher told the class that if they averaged at least 75% on their final exam, they could have a pizza party. Everyone took the exam on Monday, except for William, who was allowed to take it on Tuesday. If there are 30 people in the class, and the average before he took the test was a 74%, what score does he have to get to make sure they get to have a pizza party?"""
    # Define the total number of students in the class and the desired average score
    total_students = 30
    desired_average = 0.75

    # Calculate the sum of scores before William took the test
    sum_scores_before = 74 * (total_students - 1)

    # Calculate the minimum score William needs to achieve to reach the desired average
    min_score = (desired_average * total_students) - sum_scores_before

    # Return the minimum score William needs to achieve
    result = min_score
    return result

print(solution())