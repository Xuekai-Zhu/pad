def solution():
    """Cathy and Chris got summer jobs at the cake shop and were supposed to work 20 hours per week each for 2 months. During that time, Chris got sick for one week and Cathy took her shifts. If there are four weeks in a month, how many hours did Cathy work during the 2 months?"""
    # Define the number of hours each person is supposed to work per week
    HOURS_PER_WEEK = 20

    # Define the number of weeks in 2 months
    WEEKS_IN_2_MONTHS = 8

    # Calculate the total number of hours each person is supposed to work over the 2 months
    total_hours_per_person = HOURS_PER_WEEK * WEEKS_IN_2_MONTHS

    # Calculate the number of hours Cathy worked while covering for Chris
    cathy_covered = HOURS_PER_WEEK

    # Calculate the total number of hours Cathy worked during the 2 months
    cathy_total_hours = total_hours_per_person + cathy_covered

    result = cathy_total_hours
    return result

print(solution())