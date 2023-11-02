def solution():
    """Cathy and Chris got summer jobs at the cake shop and were supposed to work 20 hours per week each for 2 months. During that time, Chris got sick for one week and Cathy took her shifts. If there are four weeks in a month, how many hours did Cathy work during the 2 months?"""
    
    # Define the number of weeks in a month
    WEEKS_IN_MONTH = 4
    
    # Define the number of hours Cathy and Chris were supposed to work per week
    HOURS_PER_WEEK = 20
    
    # Calculate the total number of hours each of them were supposed to work 
    total_hours_per_person = HOURS_PER_WEEK * WEEKS_IN_MONTH * 2
    
    # Calculate the number of hours Chris missed due to sickness
    hours_missed = HOURS_PER_WEEK * WEEKS_IN_MONTH
    
    # Calculate the total number of hours worked by Cathy 
    hours_worked_by_cathy = total_hours_per_person + hours_missed
    
    # Display the total number of hours worked by Cathy over the 2 month period
    result = hours_worked_by_cathy
    return result

print(solution())