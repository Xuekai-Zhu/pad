def solution():
    small_pandas = 4
    small_panda_bamboo = 25
    
    big_pandas = 5
    big_panda_bamboo = 40
    
    days_per_week = 7

    # Calculate the total amount of bamboo sprouts that small pandas eat per week
    small_panda_weekly_bamboo = small_panda_bamboo * days_per_week * small_pandas

    # Calculate the total amount of bamboo sprouts that big pandas eat per week
    big_panda_weekly_bamboo = big_panda_bamboo * days_per_week * big_pandas

    # Calculate the total amount of bamboo sprouts that all pandas (small and big) eat per week
    total_panda_weekly_bamboo = small_panda_weekly_bamboo + big_panda_weekly_bamboo
    result = total_panda_weekly_bamboo
    return result

print(solution())