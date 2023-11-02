def solution():
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

    # Calculate the number of exams left to grade on Wednesday
    wednesday_exams = remaining_exams

    result = wednesday_exams
    return result

print(solution())