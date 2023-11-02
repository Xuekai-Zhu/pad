def solution():
    hours_weekday = 5 * 5  # Mitch works 5 hours every day from Monday to Friday
    hours_weekend = 3 * 2  # Mitch works 3 hours every Saturday and Sunday and earns double
    total_hours = hours_weekday + hours_weekend  # Calculate the total number of hours Mitch works every week

    # Calculate Mitch's earnings for the weekday hours
    earnings_weekday = hours_weekday * 3  # Mitch earns $3 per hour

    # Calculate Mitch's earnings for the weekend hours
    earnings_weekend = hours_weekend * 6  # Mitch earns double, so she earns $6 per hour

    # Calculate the total earnings for the week
    total_earnings = earnings_weekday + earnings_weekend

    result = total_earnings
    return result

print(solution())