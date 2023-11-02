def solution():
    # Total number of miles Iggy runs from Monday to Friday
    total_miles = 3 + 4 + 6 + 8 + 3

    # Total number of minutes Iggy spends running
    total_minutes = total_miles * 10

    # Convert minutes to hours
    total_hours = total_minutes / 60
    result = total_hours
    return result

print(solution())