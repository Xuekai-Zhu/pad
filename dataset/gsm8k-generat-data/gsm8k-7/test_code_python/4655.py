def solution():
    total_hours_per_week = 7.5
    practice_hours_per_day = 1.43  # 86 minutes converted to hours

    # Calculate the number of days Adah practiced for 86 minutes
    num_days_practiced = 2

    # Calculate the total number of hours Adah practiced for 86 minutes
    total_practice_hours = num_days_practiced * practice_hours_per_day

    # Calculate the number of hours Adah practiced on the other days
    other_practice_hours = total_hours_per_week - total_practice_hours

    # Convert the number of hours to minutes
    total_practice_minutes = other_practice_hours * 60

    result = total_practice_minutes
    return result

print(solution())