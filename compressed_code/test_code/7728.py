def solution():
    
    total_students = 81
    striped_shirts = (2/3) * total_students
    checkered_shirts = total_students - striped_shirts
    shorts = checkered_shirts + 19
    difference = striped_shirts - shorts
    result = difference
    return result

print(solution())