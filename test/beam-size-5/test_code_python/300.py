def solution():
    
    # Define the number of hours Watson works each day
    HOURS_PER_DAY = 10

    # Define the number of days Watson works each week
    DAYS_PER_WEEK = 5

    # Define Watson's hourly wage and bonus
    HOURLY_WAGE = 10
    BONUS_WAGE = 300

    # Calculate Watson's earnings in April
    earnings = (HOURS_PER_DAY * DAYS_PER_WEEK * HOURLY_WAGE) + BONUS_WAGE

    # Display Watson's earnings
    result = earnings
    return result

print(solution())