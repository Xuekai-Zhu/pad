def solution():
    adult_daily_bamboo = 138
    baby_daily_bamboo = 50
    days_in_week = 7

    # Calculate the total amount of bamboo eaten by one adult panda in a week
    adult_weekly_bamboo = adult_daily_bamboo * days_in_week

    # Calculate the total amount of bamboo eaten by one baby panda in a week
    baby_weekly_bamboo = baby_daily_bamboo * days_in_week

    # Calculate the total amount of bamboo eaten by both pandas in a week
    total_weekly_bamboo = adult_weekly_bamboo + baby_weekly_bamboo
    result = total_weekly_bamboo
    return result

print(solution())