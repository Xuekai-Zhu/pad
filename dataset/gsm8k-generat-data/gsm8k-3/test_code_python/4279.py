def solution():
    """Bill had to finish a project from work that was to take him 4 days. If he took 6 seven-hour naps in the four days, how long did he spend working on the project?"""
    # Define the total number of hours in 4 days
    TOTAL_HOURS = 4 * 24

    # Define the total hours Bill spent napping
    NAP_HOURS = 6 * 7

    # Calculate the total number of hours Bill spent working
    working_hours = TOTAL_HOURS - NAP_HOURS

    # Display the number of hours Bill spent working
    result = working_hours
    return result

print(solution())