def solution():
    """John sends his son to prep school.  It cost $20,000 per semester.  There are 2 semesters in the year.  How much does it cost to send the kid to 13 years of school?"""
    # Define the cost per semester and the number of semesters in a year
    COST_PER_SEMESTER = 20000
    SEMESTERS_PER_YEAR = 2

    # Calculate the total cost for one year of school
    year_cost = COST_PER_SEMESTER * SEMESTERS_PER_YEAR

    # Calculate the total cost for 13 years of school
    total_cost = year_cost * 13

    # Display the total cost
    result = total_cost
    return result

print(solution())