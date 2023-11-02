def solution():
    """John sends his son to prep school. It costs $20,000 per semester. There are 2 semesters in the year. How much does it cost to send the kid to 13 years of school?"""
    # Define the cost per semester and the number of semesters in a year
    COST_PER_SEMESTER = 20000
    SEMESTERS_PER_YEAR = 2

    # Calculate the total cost of sending the kid to school for 13 years
    total_cost = 13 * SEMESTERS_PER_YEAR * COST_PER_SEMESTER

    # Return the result
    result = total_cost
    return result

print(solution())