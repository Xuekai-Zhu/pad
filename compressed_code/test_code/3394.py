def solution():
    
    total_time = 24  
    sleeping_time = total_time * (1/3)
    school_time = total_time * (1/6)
    making_assignments_time = total_time * (1/12)
    family_time = total_time - sleeping_time - school_time - making_assignments_time
    result = family_time
    return result

print(solution())