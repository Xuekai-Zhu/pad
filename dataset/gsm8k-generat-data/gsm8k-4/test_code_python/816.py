def solution():
    """Matt needs to buy new plates for his home. He only wants to do dishes once a week. Three days a week it is only him and his son eating and they use 1 plate each. On the remainder of the days, his parents join them and everyone uses 2 plates that day. How many plates does he need to buy?"""
    # Define the number of days in a week
    DAYS_PER_WEEK = 7

    # Define the number of plates used by Matt and his son on a typical day
    plates_per_day = 1

    # Define the number of plates used by everyone on the days Matt's parents are visiting
    plates_per_family_day = 2

    # Define the number of days when it's just Matt and his son
    matt_and_son_days = 3

    # Calculate the number of family days in a week
    family_days = DAYS_PER_WEEK - matt_and_son_days

    # Calculate the total number of plates used in a week
    total_plates = (matt_and_son_days * plates_per_day) + (family_days * plates_per_family_day)

    # Calculate the number of plates Matt needs to buy
    plates_to_buy = total_plates - plates_per_day

    result = plates_to_buy
    return result

print(solution())