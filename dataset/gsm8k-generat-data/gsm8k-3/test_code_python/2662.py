def solution():
    """The students at Evelyn's school are keeping journals. They have 3 journal-writing sessions per week. Each student writes 4 pages in each session. How many journal pages will each student write in 6 weeks?"""
    # Define the number of journal writing sessions per week and pages per session
    SESSIONS_PER_WEEK = 3
    PAGES_PER_SESSION = 4

    # Calculate the number of journal pages each student will write in a week
    pages_per_week = SESSIONS_PER_WEEK * PAGES_PER_SESSION

    # Calculate the total number of journal pages each student will write in 6 weeks
    total_pages = pages_per_week * 6

    # Display the total number of journal pages
    result = total_pages
    return result

print(solution())