def solution():
    total_exams = 120  # Mrs. Watson has 120 final exams to grade
    monday_grading = 0.6  # Mrs. Watson will grade 60% of the exams on Monday
    tuesday_grading = 0.75  # Mrs. Watson will grade 75% of the remaining exams on Tuesday

    # Calculate the number of exams graded on Monday
    monday_exams = total_exams * monday_grading

    # Calculate the number of exams remaining after Monday's grading
    remaining_exams = total_exams - monday_exams

    # Calculate the number of exams graded on Tuesday
    tuesday_exams = remaining_exams * tuesday_grading

    # Calculate the number of exams remaining after Tuesday's grading
    remaining_exams = remaining_exams - tuesday_exams

    # Calculate the number of exams Mrs. Watson needs to grade on Wednesday
    wednesday_exams = remaining_exams
    result = wednesday_exams
    return result

print(solution())