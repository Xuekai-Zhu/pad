def solution():
    gallons_per_day = 1.5  # John drinks 1.5 gallons of water per day
    days_per_week = 7  # There are 7 days in a week

    # Calculate the total number of gallons John drinks in a week
    total_gallons = gallons_per_day * days_per_week

    # Convert the total number of gallons to quarts
    quarts = total_gallons * 4
    result = quarts
    return result

print(solution())