def solution():
    num_students = 10
    desired_average = 85

    # Calculate the total score of the 9 students who have already taken the test
    total_score = (5 * 92) + (4 * 80)

    # Calculate the minimum score the last student needs to achieve to reach the desired average
    min_score = (desired_average * num_students) - total_score

    result = min_score
    return result

print(solution())