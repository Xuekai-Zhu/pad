def solution():
    
    # Define the number of hours Josh spent working out each week
    WEEKLY_HOURS = 4

    # Define the number of hours Josh spent working out each subsequent week
    WEEKLY_HOURS_1 = 5
    WEEKLY_HOURS_2 = 5
    WEEKLY_HOURS_3 = 6

    # Define the number of weeks Josh worked out
    WEEKS = 8

    # Calculate the total number of hours Josh spent working out
    total_hours = (WEEKLY_HOURS * WEEKLY_HOURS) + (WEEKLY_HOURS_1 * WEEKLY_HOURS_2) + (WEEKLY_HOURS_3 * WEEKLY_HOURS_3)

    # Display the total number of hours
    result = total_hours
    return result

print(solution())