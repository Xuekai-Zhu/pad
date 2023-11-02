def solution():
    """Kelly booked a three week vacation to visit relatives. The first day, she spent traveling. The next 5 days she spent at her Grandparents' house. The next day, she spent traveling. Then, she spends the next 5 days at her brother's house. Then she spent two days traveling to her sister's house, spent several days at her sister's house, and then spent two more days traveling home. How many days did she spend at her sister's house?"""
    total_days = 21
    grandparents_days = 5
    brother_days = 5
    travel_days = 6
    sister_travel_days = 2
    sister_days = total_days - 1 - grandparents_days - brother_days - travel_days - sister_travel_days - 2
    result = sister_days
    return result

print(solution())