def solution():
    """A psychiatrist has 4 patients that need 25 sessions in total. One of the patients needs 6 sessions. Another patient needs 5 more than that. How many sessions would the remaining patients need?"""
    total_sessions = 25
    patient1_sessions = 6
    patient2_sessions = patient1_sessions + 5
    remaining_sessions = total_sessions - patient1_sessions - patient2_sessions
    result = remaining_sessions
    return result

print(solution())