def solution():
    water_per_medication = 4  # Kara has to drink 4 ounces of water with each medication
    medications_per_day = 3  # Kara takes one tablet three times a day
    days_in_week = 7  # There are 7 days in a week
    total_days = 14  # Kara followed the instructions for one week, then missed twice in the second week

    # Calculate the total number of ounces of water Kara drinks in the first week
    ounces_first_week = water_per_medication * medications_per_day * days_in_week

    # Calculate the total number of ounces of water Kara drinks in the second week
    ounces_second_week = water_per_medication * medications_per_day * (total_days - days_in_week - 2)

    # Calculate the total number of ounces of water Kara drinks over the two weeks
    total_ounces = ounces_first_week + ounces_second_week
    result = total_ounces
    return result

print(solution())