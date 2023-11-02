def solution():
    """Jessica just got her driving permit. She must complete 50 hours of driving with a parent to get her driver’s license. It takes 20 minutes to drive to school. If she drives to and from school every day, how many school days will it take Jessica to meet the 50-hour driving requirement?"""
    hours_per_day = 40/60 # Convert 40 minutes to hours
    days_needed = 50 / hours_per_day / 2 # Divide by 2 to account for round trip
    result = days_needed
    return result

print(solution())