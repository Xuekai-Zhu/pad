def solution():
    """A psychiatrist has 4 patients that need 25 sessions in total. One of the patients needs 6 sessions. Another patient needs 5 more than that. How many sessions would the remaining patients need?"""
    # Define the total number of sessions and the number of sessions needed by the first two patients
    total_sessions = 25
    first_patient_sessions = 6
    second_patient_sessions = first_patient_sessions + 5

    # Calculate the number of sessions needed by the remaining two patients
    remaining_sessions = total_sessions - first_patient_sessions - second_patient_sessions

    # Return the result
    result = remaining_sessions
    return result

print(solution())