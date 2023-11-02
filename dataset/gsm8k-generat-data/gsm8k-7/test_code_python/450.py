def solution():
    total_gallons = 105
    weeks = 3
    total_days = weeks * 7

    # Calculate how many gallons Flora would drink if she drank 3 gallons daily
    daily_gallons = 3
    total_gallons_drunk = daily_gallons * total_days

    # Calculate how many more gallons Flora needs to drink to reach Dr. Juan's requirement
    gallons_needed = total_gallons - total_gallons_drunk
    additional_daily_gallons = gallons_needed / total_days
    result = additional_daily_gallons
    return result

print(solution())