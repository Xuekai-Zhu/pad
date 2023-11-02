def solution():
    
    first_hospital_patients_per_week = 20 * 5
    second_hospital_patients_per_week = round(1.2 * 20) * 5
    total_patients_per_week = first_hospital_patients_per_week + second_hospital_patients_per_week
    total_patients_per_year = total_patients_per_week * 50
    result = total_patients_per_year
    return result

print(solution())