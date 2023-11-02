def solution():
    """Jason goes to the library 4 times more often than William goes. If William goes 2 times per week to the library, how many times does Jason go to the library in 4 weeks?"""
    # Define William's library visits per week
    william_visits_per_week = 2

    # Calculate Jason's library visits per week
    jason_visits_per_week = 4 * william_visits_per_week

    # Calculate Jason's library visits in 4 weeks
    jason_visits_4_weeks = jason_visits_per_week * 4

    result = jason_visits_4_weeks
    return result

print(solution())