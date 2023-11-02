def solution():
    patients_first_hospital = 20
    patients_second_hospital = 20 + (20 * 0.2)
    total_patients = (patients_first_hospital + patients_second_hospital) * 5
    result = total_patients
    return result

print(solution())