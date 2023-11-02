def solution():
    # Calculate the total score of the students who took the test
    total_score = 77 * 24  # 24 students took the test

    # Calculate the minimum score the absent student needs to receive for the average to be at least 75%
    minimum_score = (25*75) - total_score

    result = minimum_score
    return result

print(solution())