def solution():
    conventional_doctors_diagnosis = "could lose singing career"
    holistic_doctor_diagnosis = "simple acid reflux"
    if holistic_doctor_diagnosis in conventional_doctors_diagnosis.lower():
        result = "yes"
    else:
        result = "no"
    return result

print(solution())