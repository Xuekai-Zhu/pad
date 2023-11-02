def solution():
    """The students at Evelyn's school are keeping journals. They have 3 journal-writing sessions per week. Each student writes 4 pages in each session. How many journal pages will each student write in 6 weeks?"""
    # Define the number of journal-writing sessions per week and the number of pages written per session
    sessions_per_week = 3
    pages_per_session = 4

    # Calculate the total number of journal pages written by each student per week
    pages_per_week = sessions_per_week * pages_per_session

    # Calculate the total number of journal pages written by each student in 6 weeks
    pages_in_six_weeks = pages_per_week * 6

    # return the result
    result = pages_in_six_weeks
    return result

print(solution())