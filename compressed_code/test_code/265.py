def solution():
    
    total_patients = 12
    standard_care_patients = 8
    special_diet_patients = total_patients - standard_care_patients
    special_diet_time = 1.2 * 5 
    total_time = (standard_care_patients * 5) + (special_diet_patients * special_diet_time)
    result = total_time
    return result

print(solution())