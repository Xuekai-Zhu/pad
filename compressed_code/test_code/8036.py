def solution():
    
    johnson_students = 30
    johnson_goldfish = 1/6 * johnson_students
    feldstein_students = 30
    feldstein_goldfish = 2/3 * feldstein_students
    henderson_students = 30
    henderson_goldfish = 1/5 * henderson_students
    total_goldfish = johnson_goldfish + feldstein_goldfish + henderson_goldfish
    result = total_goldfish
    return result

print(solution())