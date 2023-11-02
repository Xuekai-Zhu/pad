def solution():
    """There are 64 seventh graders at a middle school. This is 32% of the students at the school. The sixth graders comprise 38% of the students. How many sixth graders attend middle school?"""
    seventh_grade_percent = 32
    sixth_grade_percent = 38
    total_students = int(64 / (seventh_grade_percent / 100))
    sixth_graders = int(total_students * (sixth_grade_percent / 100))
    result = sixth_graders
    return result

print(solution())