def solution():
    """Four small panda bears and five bigger panda bears eat 25 pounds and 40 pounds of fresh bamboo sprouts every day, respectively. How many pounds of bamboo do the 9 pandas eat in a week?"""
    # Define the number of small and big pandas, and the amount of bamboo they eat per day
    small_pandas = 4
    big_pandas = 5
    small_panda_bamboo = 25
    big_panda_bamboo = 40

    # Find the total amount of bamboo eaten per day by all pandas
    total_bamboo = (small_pandas * small_panda_bamboo) + (big_pandas * big_panda_bamboo)

    # Find the total amount of bamboo eaten in a week
    weekly_bamboo = total_bamboo * 7

    result = weekly_bamboo
    return result

print(solution())