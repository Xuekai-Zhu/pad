def solution():
    """A psychiatrist has 4 patients that need 25 sessions in total. One of the patients needs 6 sessions. Another patient needs 5 more than that. How many sessions would the remaining patients need?"""
    # Define the total number of sessions needed and the number of sessions needed for the first two patients
    total_sessions = 25
    patient1_sessions = 6
    patient2_sessions = patient1_sessions + 5

    # Calculate the total number of remaining sessions needed
    remaining_sessions = total_sessions - patient1_sessions - patient2_sessions

    # Calculate the number of sessions needed per remaining patient
    remaining_patients = 4 - 2
    remaining_per_patient = remaining_sessions / remaining_patients

    # Display the number of sessions needed per remaining patient
    result = remaining_per_patient
    return result

print(solution())