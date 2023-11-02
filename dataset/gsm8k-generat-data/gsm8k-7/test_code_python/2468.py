def solution():
    total_sessions = 25
    patient1_sessions = 6
    patient2_sessions = patient1_sessions + 5

    # Calculate the total number of sessions needed for the remaining patients
    total_patient_sessions = total_sessions - (patient1_sessions + patient2_sessions)
    result = total_patient_sessions
    return result

print(solution())