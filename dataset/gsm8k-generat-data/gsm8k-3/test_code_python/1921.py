def solution():
    """Lisa has 36 candies. On Mondays and Wednesdays, she eats 2 candies for each day
    and on the other days of the week she eats 1 candy for each day. How many weeks does it take for Lisa to eat all of the candies?"""
    # Define the number of candies Lisa has and the number of candies she eats per day
    LISA_CANDIES = 36
    MON_WED_CANDY_EAT = 2
    OTHER_DAYS_CANDY_EAT = 1
    TOTAL_CANDY_EAT = (MON_WED_CANDY_EAT * 2) + (OTHER_DAYS_CANDY_EAT * 5)

    # Calculate the number of weeks it takes for Lisa to eat all the candies
    weeks = 0
    while LISA_CANDIES > 0:
        LISA_CANDIES -= TOTAL_CANDY_EAT
        weeks += 1

    # Display the number of weeks
    result = weeks
    return result

print(solution())