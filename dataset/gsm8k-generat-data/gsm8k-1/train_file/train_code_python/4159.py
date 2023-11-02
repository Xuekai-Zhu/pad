def solution():
    """Hannah harvests 5 strawberries daily for the next whole month of April, which has 30 days. If she gives away 20 strawberries to her friends and 30 strawberries are stolen, how many strawberries does she have by the end of April?"""
    strawberries_per_day = 5
    days_in_april = 30
    total_strawberries = strawberries_per_day * days_in_april
    strawberries_given_away = 20
    strawberries_stolen = 30
    remaining_strawberries = total_strawberries - strawberries_given_away - strawberries_stolen
    result = remaining_strawberries
    return result

print(solution())