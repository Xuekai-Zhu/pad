def solution():
    """A retail store wants to hire 50 new phone reps to assist with the increased call volume that they will experience over the holiday.  Each phone rep will work 8 hours a day and will be paid $14.00 an hour.  After 5 days, how much will the company pay all 50 new employees?"""
    # Define the number of new phone reps hired
    NUM_REPS = 50

    # Define the number of hours worked per day and hourly rate
    HOURS_PER_DAY = 8
    HOURLY_RATE = 14

    # Define the number of days worked
    DAYS_WORKED = 5

    # Calculate the total amount paid to all 50 phone reps after 5 days
    total_payment = NUM_REPS * HOURS_PER_DAY * HOURLY_RATE * DAYS_WORKED

    # Display the total payment
    result = total_payment
    return result

print(solution())