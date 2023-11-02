def solution():
    num_exams = 120
    monday_grading = 0.6
    tuesday_grading = 0.75

    # Calculate the number of exams graded on Monday
    monday_count = num_exams * monday_grading

    # Calculate the number of exams left to be graded after Monday
    remaining_exams = num_exams - monday_count

    # Calculate the number of exams graded on Tuesday
    tuesday_count = remaining_exams * tuesday_grading

    # Calculate the number of exams left to be graded on Wednesday
    wednesday_count = num_exams - monday_count - tuesday_count
    result = wednesday_count
    return result

print(solution())