def solution():
    num_math_classes = 6
    num_math_students_per_class = 5
    num_teachers = 13
    num_volunteers_needed = 50

    # Calculate the total number of math students who have volunteered to help
    total_math_students = num_math_classes * num_math_students_per_class

    # Calculate the total number of volunteers who have already signed up
    total_volunteers = total_math_students + num_teachers

    # Calculate the number of additional volunteers needed
    remaining_volunteers_needed = num_volunteers_needed - total_volunteers
    result = remaining_volunteers_needed
    return result

print(solution())