def solution():
    patient_age = "teenager"
    has_depression = True
    # Check if the patient is a teenager or young adult with depression
    if patient_age == "teenager" and has_depression:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())