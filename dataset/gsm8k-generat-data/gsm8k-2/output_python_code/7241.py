def solution():
    """John drinks 1.5 gallons of water a day. How many quarts does he drink a week?"""
    daily_gallons = 1.5
    weekly_gallons = daily_gallons * 7
    quarts_per_gallon = 4
    weekly_quarts = weekly_gallons * quarts_per_gallon
    result = weekly_quarts
    return result

print(solution())