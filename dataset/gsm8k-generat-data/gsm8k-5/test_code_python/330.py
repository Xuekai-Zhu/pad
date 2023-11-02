def solution():
    expected_attendance = 220  # Laura expects 220 people to attend
    percentage_not_attending = 5  # Approximately 5% typically don't show
    actual_attendance = expected_attendance * (100 - percentage_not_attending) / 100  # Calculate actual attendance

    result = actual_attendance
    return result

print(solution())