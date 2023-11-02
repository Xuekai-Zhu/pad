def solution():
    number_of_patients_per_hour = 8
    number_of_hours = 8
    number_of_toothbrushes = 2
    number_of_days = 5
    total_number_of_patients = number_of_patients_per_hour * number_of_hours * number_of_days
    total_number_of_toothbrushes = total_number_of_patients * number_of_toothbrushes
    result = total_number_of_toothbrushes
    
    return result

print(solution())