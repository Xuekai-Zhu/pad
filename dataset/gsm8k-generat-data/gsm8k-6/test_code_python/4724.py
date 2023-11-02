def solution():
    # Calculate the number of exams that Mrs. Watson graded on Monday
    exams_graded_Monday = 0.6 * 120
    # Calculate the number of exams remaining to be graded after Monday
    exams_remaining = 120 - exams_graded_Monday
    # Calculate the number of exams that Mrs. Watson graded on Tuesday
    exams_graded_Tuesday = 0.75 * exams_remaining
    # Calculate the number of exams remaining to be graded after Tuesday
    exams_remaining_Wednesday = exams_remaining - exams_graded_Tuesday
    result = exams_remaining_Wednesday
    return result

print(solution())