def solution():
    """On each of 7 Mondays, it rained 1.5 centimeters. On each of 9 Tuesdays it rained 2.5 centimeters. How many more centimeters did it rain on Tuesdays than Mondays?"""
    monday_rain = 1.5
    tuesday_rain = 2.5
    monday_total = monday_rain * 7
    tuesday_total = tuesday_rain * 9
    difference = tuesday_total - monday_total
    result = difference
    return result

print(solution())