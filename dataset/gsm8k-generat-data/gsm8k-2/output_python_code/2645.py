def solution():
    """John sends his son to prep school. It cost $20,000 per semester. There are 2 semesters in the year. How much does it cost to send the kid to 13 years of school?"""
    semesters_per_year = 2
    semesters_per_school_year = semesters_per_year * 13
    cost_per_semester = 20000
    total_cost = semesters_per_school_year * cost_per_semester
    result = total_cost
    return result

print(solution())