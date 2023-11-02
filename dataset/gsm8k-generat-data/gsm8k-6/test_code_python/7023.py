def solution():
    # Calculate the total number of miles that Iggy runs from Monday to Friday
    total_miles = 3 + 4 + 6 + 8 + 3

    # Calculate the total time in minutes that Iggy spends running from Monday to Friday
    total_time = total_miles * 10  # Iggy runs at a pace of 1 mile in 10 minutes

    # Convert the total time from minutes to hours
    total_hours = total_time / 60

    result = total_hours
    return result

print(solution())