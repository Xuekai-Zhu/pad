def solution():
    # Calculate the total number of points earned by the students who took the test
    total_points = 77 * 24

    # Calculate the total number of points needed for the class to achieve an average score of 75%
    target_points = 75 * 25

    # Calculate the minimum score the absent student needs in order for the class to achieve the target average
    min_score = (target_points - total_points) / 1

    result = min_score
    return result

print(solution())