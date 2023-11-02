def solution():
    num_sessions_per_week = 3
    num_pages_per_session = 4
    num_weeks = 6

    # Calculate the total number of journal-writing sessions
    total_sessions = num_sessions_per_week * num_weeks

    # Calculate the total number of journal pages per student
    total_pages = total_sessions * num_pages_per_session
    result = total_pages
    return result

print(solution())