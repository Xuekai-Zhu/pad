def solution():
    """Nedy can eat 8 packs of crackers from Monday to Thursday. If Nedy ate twice the amount on Friday, how many crackers did Nedy eat in all?"""
    # Define the number of crackers Nedy can eat from Monday to Thursday
    crackers_mon_to_thurs = 8

    # Calculate the total number of crackers Nedy ate from Monday to Thursday
    total_crackers_mon_to_thurs = crackers_mon_to_thurs * 4

    # Calculate the number of crackers Nedy ate on Friday
    crackers_friday = crackers_mon_to_thurs * 2

    # Calculate the total number of crackers Nedy ate in all
    total_crackers = total_crackers_mon_to_thurs + crackers_friday

    result = total_crackers
    return result

print(solution())