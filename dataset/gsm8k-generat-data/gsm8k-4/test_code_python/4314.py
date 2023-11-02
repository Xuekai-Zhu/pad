def solution():
    """Carla needs to dry-clean 80 pieces of laundry by noon. If she starts work at 8 AM, how many pieces of laundry does she need to clean per hour?"""
    # Define the number of hours available for cleaning
    hours_available = 4

    # Calculate the number of pieces of laundry to clean per hour
    pieces_per_hour = 80 / hours_available

    # Round the result to the nearest whole number
    pieces_per_hour = round(pieces_per_hour)

    # Return the result
    result = pieces_per_hour
    return result

print(solution())