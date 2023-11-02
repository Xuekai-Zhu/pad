def solution():
    
    num_patients = 12
    num_special = num_patients // 3
    standard_time = 5
    special_time = standard_time * 1.2
    total_time = (num_patients - num_special) * standard_time + num_special * special_time
    result = total_time
    return result

print(solution())