def solution():
    """The students at Evelyn's school are keeping journals. They have 3 journal-writing sessions per week. Each student writes 4 pages in each session. How many journal pages will each student write in 6 weeks?"""
    sessions_per_week = 3
    pages_per_session = 4
    weeks = 6
    total_pages = sessions_per_week * pages_per_session * weeks
    result = total_pages
    return result

print(solution())