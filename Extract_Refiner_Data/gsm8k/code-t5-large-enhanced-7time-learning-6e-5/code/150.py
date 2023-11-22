def solution():
    
    # Define the number of hours Kimo spends attending each day
    MON_WED_FRI_HOURS = 3
    TUE_THU_HOURS = 2

    # Define the number of days in a week
    WEEKS_PER_WEEK = 7

    # Define the number of weeks in a semester
    WEEKS_PER_SEMESTER = 16

    # Calculate the total number of hours Kimo spends attending classes
    total_hours = MON_WED_FRI_HOURS * 3 + TUE_THU_HOURS * 2 * WEEKS_PER_WEEK

    # Display the total number of hours Kimo spends attending classes
    result = total_hours
    return result

print(solution())