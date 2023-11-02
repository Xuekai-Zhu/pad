def solution():
    """Kelly booked a three week vacation to visit relatives. The first day, she spent traveling. The next 5 days she spent at her Grandparents' house. The next day, she spent traveling. Then, she spends the next 5 days at her brother's house. Then she spent two days traveling to her sister's house, spent several days at her sister's house, and then spent two more days traveling home. How many days did she spend at her sister's house?"""
    # Define the total number of days for the vacation
    total_days = 21

    # Calculate the days for traveling and visiting Grandparents and brother
    travel_days = 1 + 1 + 2
    grandparents_days = 5
    brother_days = 5

    # Calculate the days for visiting sister
    sister_days = total_days - travel_days - grandparents_days - brother_days - 2

    # return the result
    result = sister_days
    return result

print(solution())