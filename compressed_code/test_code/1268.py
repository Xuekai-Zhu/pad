def solution():
    
    total_class_time = 7.5 * 60  
    history_chem_time = 1.5 * 60  
    other_class_time = total_class_time - history_chem_time
    num_other_classes = 7 - 2  
    avg_other_class_time = other_class_time / num_other_classes
    result = avg_other_class_time
    return result

print(solution())