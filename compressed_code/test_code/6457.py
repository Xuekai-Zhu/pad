def solution():
    
    total_students = 25
    fries = 15
    burgers = 10
    both = 6
    neither = total_students - (fries + burgers - both)
    result = neither
    return result

print(solution())