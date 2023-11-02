def solution():
    """The teacher told the class that if they averaged at least 75% on their final exam, they could have a pizza party. Everyone took the exam on Monday, except for William, who was allowed to take it on Tuesday. If there are 30 people in the class, and the average before he took the test was a 74%, what score does he have to get to make sure they get to have a pizza party?"""
    # Define the number of students and the desired average
    num_students = 30
    desired_average = 0.75

    # Calculate the sum of the scores before William took the test
    initial_sum = num_students * 0.74

    # Calculate the minimum score William needs to get
    min_score = (desired_average * (num_students + 1)) - initial_sum

    # Display the minimum score William needs to get
    result = min_score
    return result

print(solution())