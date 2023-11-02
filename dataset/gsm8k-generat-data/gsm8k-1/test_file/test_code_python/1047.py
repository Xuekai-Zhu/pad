def solution():
    """Ingrid drinks 8 cups of water every day. If there are 16 cups in a gallon, how many gallons of water does she drink in 30 days?"""
    cups_per_day = 8
    cups_per_gallon = 16
    days = 30
    total_cups = cups_per_day * days
    total_gallons = total_cups / cups_per_gallon
    result = total_gallons
    return result

print(solution())