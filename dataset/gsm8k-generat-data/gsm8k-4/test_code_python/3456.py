def solution():
    """The teacher divided the students into four groups. One group had 5 students, another 8 students, and the third 7 students. If there were 24 total students, how many students were in the fourth group?"""
    # Define the total number of students and the number of students in the first three groups
    total_students = 24
    group_1 = 5
    group_2 = 8
    group_3 = 7

    # Calculate the number of students in the fourth group
    group_4 = total_students - group_1 - group_2 - group_3

    # Return the result
    result = group_4
    return result

print(solution())