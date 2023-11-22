def solution():
    
    # Define the number of days they ride their bikes each week
    days_per_week = 7

    # Define the number of times they ride their bikes each day
    daily_riders = 3

    # Calculate the number of times they ride their bikes each week
    weekly_riders = (daily_riders * 5) + (daily_riders * 2)

    # Display the number of times they ride their bikes each week
    result = weekly_riders
    return result

print(solution())