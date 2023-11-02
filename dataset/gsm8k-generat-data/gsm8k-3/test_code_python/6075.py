def solution():
    """Tim hires two bodyguards. They each charge $20 an hour. He hires them for 8 hour per day. How much does he pay them in a week if he hires them 7 days a week?"""
    # Define the hourly rate for each bodyguard
    HOURLY_RATE = 20

    # Define the number of hours worked by each bodyguard per day
    HOURS_PER_DAY = 8

    # Define the number of bodyguards
    NUM_BODYGUARDS = 2

    # Define the number of days worked per week
    DAYS_PER_WEEK = 7

    # Calculate the total cost per hour for both bodyguards
    total_hourly_rate = HOURLY_RATE * NUM_BODYGUARDS

    # Calculate the total cost per day for both bodyguards
    daily_cost = total_hourly_rate * HOURS_PER_DAY

    # Calculate the total cost per week for both bodyguards
    weekly_cost = daily_cost * DAYS_PER_WEEK

    # Display the total cost per week
    result = weekly_cost
    return result

print(solution())