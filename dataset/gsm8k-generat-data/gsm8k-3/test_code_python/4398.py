def solution():
    """An adult panda can eat 138 pounds of bamboo each day. A baby panda can eat 50 pounds of bamboo a day.  How many pounds of bamboo will the pandas eat in a week?"""
    # Define the amount of bamboo eaten by each panda per day
    ADULT_BAMBOO_PER_DAY = 138
    BABY_BAMBOO_PER_DAY = 50

    # Calculate the total amount of bamboo eaten by both pandas in a day
    total_bamboo_per_day = ADULT_BAMBOO_PER_DAY + BABY_BAMBOO_PER_DAY

    # Calculate the total amount of bamboo eaten by both pandas in a week (7 days)
    total_bamboo_per_week = total_bamboo_per_day * 7

    # Display the total amount of bamboo eaten in a week
    result = total_bamboo_per_week
    return result

print(solution())