def solution():
    
    # Define the total number of students and the number of groups
    total_students = 50
    num_groups = 6

    # Calculate the number of students per group
    students_per_group = total_students / num_groups

    # Calculate the number of additional groups needed to form the students
    additional_groups = students_per_group - students_per_group

    # return the result
    result = additional_groups
    return result

print(solution())