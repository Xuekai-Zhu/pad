def solution():
    """Mrs. Watson is grading 120 final exams from her American History class. On Monday, she grades 60% of the exams. On Tuesday, she grades 75% of the remaining exams. On Wednesday, how many more exams does she need to grade?"""
    # Define the total number of exams
    total_exams = 120

    # Calculate the number of exams graded on Monday
    monday_exams = total_exams * 0.6

    # Calculate the number of exams remaining after Monday
    remaining_exams = total_exams - monday_exams

    # Calculate the number of exams graded on Tuesday
    tuesday_exams = remaining_exams * 0.75

    # Calculate the number of exams remaining after Tuesday
    remaining_exams = remaining_exams - tuesday_exams

    # The result is the number of exams remaining after Wednesday
    result = remaining_exams
    return result

print(solution())