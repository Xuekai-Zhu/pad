def solution():
    # Define the number of total sessions needed and the number of sessions for the first patient
    total_sessions = 25
    patient1_sessions = 6

    # Calculate the sessions needed for the second patient, and the total sessions needed for the remaining patients
    patient2_sessions = patient1_sessions + 5
    remaining_sessions = total_sessions - patient1_sessions - patient2_sessions

    # Calculate the average number of sessions needed for the remaining patients
    avg_sessions = remaining_sessions / 2

    result = avg_sessions
    return result

print(solution())