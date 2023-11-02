def solution():
    """The teacher divided the students into four groups. One group had 5 students, another 8 students, and the third 7 students. If there were 24 total students, how many students were in the fourth group?"""
    # Calculate the total number of students in the first three groups
    total_students = 5 + 8 + 7

    # Calculate the number of students in the fourth group
    fourth_group = 24 - total_students

    # Display the number of students in the fourth group
    result = fourth_group
    return result

print(solution())