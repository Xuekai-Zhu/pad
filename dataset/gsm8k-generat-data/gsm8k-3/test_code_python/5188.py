def solution():
    """There are 325 students in a local high school.  40 percent of the students have glasses, how many students do not have glasses?"""
    # Define the total number of students and the percentage of students with glasses
    total_students = 325
    percent_with_glasses = 40

    # Calculate the number of students with glasses
    num_with_glasses = total_students * percent_with_glasses / 100

    # Calculate the number of students without glasses
    num_without_glasses = total_students - num_with_glasses

    # Display the number of students without glasses
    result = num_without_glasses
    return result

print(solution())