def solution():
    # Calculate the total miles Rosie runs in a week
    total_miles = 6*1 + 6*(30/60) + 6*1 + 6*(20/60)  # Rosie runs at 6 miles per hour
    remaining_miles = 20 - total_miles  # Calculate the remaining miles she needs to run

    # Convert remaining miles to minutes
    minutes_to_run = (remaining_miles / 6) * 60
    result = minutes_to_run
    return result

print(solution())