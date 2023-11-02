def solution():
    """There are 64 seventh graders at a middle school. This is 32% of the students at the school. The sixth graders comprise 38% of the students. How many sixth graders attend middle school?"""
    seventh_grade_percent = 32
    sixth_grade_percent = 38
    total_students = 100
    seventh_grade_count = (seventh_grade_percent/100) * total_students
    sixth_grade_count = total_students - seventh_grade_count
    sixth_grade_percent_of_total = (sixth_grade_count/total_students) * 100
    sixth_grade_count_final = round((sixth_grade_percent/100) * total_students)
    result = sixth_grade_count_final
    return result

print(solution())