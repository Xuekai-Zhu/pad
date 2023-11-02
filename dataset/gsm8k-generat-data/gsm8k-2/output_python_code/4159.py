def solution():
    """Hannah harvests 5 strawberries daily for the next whole month of April, which has 30 days. If she gives away 20 strawberries to her friends and 30 strawberries are stolen, how many strawberries does she have by the end of April?"""
    daily_harvest = 5
    days_in_april = 30
    total_harvest = daily_harvest * days_in_april
    given_away = 20
    stolen = 30
    remaining_strawberries = total_harvest - given_away - stolen
    result = remaining_strawberries
    return result

print(solution())