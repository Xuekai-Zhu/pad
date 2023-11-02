def solution():
    total_sessions = 25  # 4 patients need 25 sessions in total

    # One patient needs 6 sessions
    # Another patient needs 5 sessions more than the first patient
    sessions_used = 6 + (6 + 5)
    sessions_remaining = total_sessions - sessions_used

    # Calculate the average number of sessions needed by the remaining patients
    avg_sessions_remaining = sessions_remaining / 2
    result = avg_sessions_remaining
    return result

print(solution())