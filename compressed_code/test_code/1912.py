def solution():
    
    total_students = 81
    striped_shirts = (2/3) * total_students
    checkered_shirts = total_students - striped_shirts
    shorts = checkered_shirts + 19
    striped_shirts_more = striped_shirts - shorts
    result = striped_shirts_more
    return result

print(solution())