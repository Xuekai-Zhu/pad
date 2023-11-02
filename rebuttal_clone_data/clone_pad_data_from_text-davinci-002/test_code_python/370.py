def solution():
    standard_care_patients = 8
    special_care_patients = 4
    serving_time_increase = 20
    total_patients = standard_care_patients + special_care_patients
    time_per_standard_patient = 5
    time_per_special_patient = time_per_standard_patient + (time_per_standard_patient * (serving_time_increase / 100))
    total_serving_time = (time_per_standard_patient * standard_care_patients) + (time_per_special_patient * special_care_patients)
    result = total_serving_time
    return result

print(solution())