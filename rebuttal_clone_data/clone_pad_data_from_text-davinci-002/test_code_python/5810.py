def solution():
    seventh_graders = 64
    percent_seventh_graders = 32
    percent_sixth_graders = 38
    total_students = seventh_graders / (percent_seventh_graders / 100)
    sixth_graders = total_students * (percent_sixth_graders / 100)
    result = sixth_graders
    return result

print(solution())