def solution():
    total_people = 40 + 10
    total_vests = 20
    student_vests = total_vests * 0.20
    needed_vests = total_people - total_vests + student_vests
    result = needed_vests
    
    return result

print(solution())