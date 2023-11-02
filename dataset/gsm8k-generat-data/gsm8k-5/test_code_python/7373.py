def solution():
    # Calculate the total reading time for mornings and evenings
    morning_reading_time = 30  # Hank reads the newspaper for 30 minutes every weekday morning
    evening_reading_time = 60  # Hank reads part of a novel for 1 hour every weekday evening
    weekend_reading_time = 2 * (morning_reading_time + evening_reading_time)  # Hank doubles his reading time on weekends

    # Calculate the total reading time for the week
    total_reading_time = (morning_reading_time + evening_reading_time) * 5 + weekend_reading_time * 2

    # Convert the total reading time to minutes
    total_reading_time_in_minutes = total_reading_time * 60
    result = total_reading_time_in_minutes
    return result

print(solution())