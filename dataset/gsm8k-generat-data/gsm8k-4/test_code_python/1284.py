def solution():
    """John takes a 10-minute shower every other day for 4 weeks. If his shower uses 2 gallons of water per minute. How much water does he use in those 4 weeks?"""
    # Define the number of days in 4 weeks
    days_in_4_weeks = 28

    # Calculate the number of times John takes a shower in 4 weeks
    showers_in_4_weeks = 14

    # Calculate the total number of minutes John spends in the shower
    total_minutes = showers_in_4_weeks * 10

    # Calculate the total amount of water used in gallons
    water_used = total_minutes * 2

    result = water_used
    return result

print(solution())