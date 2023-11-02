def solution():
    """The teacher divided the students into four groups. One group had 5 students, another 8 students, and the third 7 students. If there were 24 total students, how many students were in the fourth group?"""
    total_students = 24
    first_group = 5
    second_group = 8
    third_group = 7
    fourth_group = total_students - first_group - second_group - third_group
    result = fourth_group
    return result

print(solution())