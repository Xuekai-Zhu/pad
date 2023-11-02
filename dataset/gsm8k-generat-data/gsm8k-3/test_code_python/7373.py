def solution():
    """Hank reads the newspaper every morning, 5 days a week for 30 minutes.  He reads part of a novel every evening, 5 days a week, for 1 hour.  He doubles his reading time on Saturday and Sundays.  How many minutes does Hank spend reading in 1 week?"""
    # Define Hank's regular reading times
    morning_reading = 30 # minutes
    evening_reading = 60 # minutes

    # Calculate Hank's reading time on weekdays
    weekday_reading = (morning_reading + evening_reading) * 5 # minutes

    # Calculate Hank's reading time on weekends
    weekend_reading = (2 * morning_reading + 2 * evening_reading) * 2 # minutes

    # Calculate Hank's total reading time in one week
    total_reading = weekday_reading + weekend_reading # minutes

    # Display Hank's total reading time
    result = total_reading
    return result

print(solution())