def solution():
    miles_per_day = [3, 4, 6, 8, 3]
    total_miles = sum(miles_per_day)

    # Calculate the total time in minutes that Iggy spends running
    time_in_minutes = total_miles * 10

    # Convert the total time to hours
    time_in_hours = time_in_minutes / 60
    result = time_in_hours
    return result

print(solution())