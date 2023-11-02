def solution():
     students_taking_exam = 80
     students_scoring_100 = 2/5 * students_taking_exam
     students_scoring_below_80 = students_taking_exam - students_scoring_100
     students_failing_exam = students_scoring_below_80 * 1/2
     result = students_failing_exam
     return result

print(solution())