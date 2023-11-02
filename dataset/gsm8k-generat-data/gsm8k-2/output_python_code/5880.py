def solution():
    """John's car gets 30 mpg. He drives 20 miles to work each way 5 days a week. He also drives another 40 miles a week for leisure travel. How many gallons of gas does he use a week?"""
    commute_miles = 20 * 2 * 5 # round trip to work, 5 days a week
    leisure_miles = 40
    total_miles = commute_miles + leisure_miles
    mpg = 30
    total_gallons = total_miles / mpg
    result = total_gallons
    return result

print(solution())