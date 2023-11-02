def solution():
    """There are 64 seventh graders at a middle school. This is 32% of the students at the school. The sixth graders comprise 38% of the students. How many sixth graders attend middle school?"""
    # Calculate the total number of students at the school
    total_students = 64 / 0.32

    # Calculate the number of sixth graders at the school
    sixth_graders = total_students * 0.38

    result = round(sixth_graders)
    return result

print(solution())