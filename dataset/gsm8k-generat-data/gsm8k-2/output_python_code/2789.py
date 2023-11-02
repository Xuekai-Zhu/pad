def solution():
    """Four small panda bears and five bigger panda bears eat 25 pounds and 40 pounds of fresh bamboo sprouts every day, respectively. How many pounds of bamboo do the 9 pandas eat in a week?"""
    small_panda_daily = 4 * 25
    big_panda_daily = 5 * 40
    total_panda_daily = small_panda_daily + big_panda_daily
    pandas_weekly = 9 * total_panda_daily
    result = pandas_weekly
    return result

print(solution())