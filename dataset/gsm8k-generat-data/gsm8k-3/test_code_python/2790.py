def solution():
    """Four small panda bears and five bigger panda bears eat 25 pounds and 40 pounds of fresh bamboo sprouts every day, respectively. How many pounds of bamboo do the 9 pandas eat in a week?"""
    # Calculate the total amount of bamboo the 4 small pandas eat in a week
    small_pandas_weekly_bamboo = 4 * 25 * 7

    # Calculate the total amount of bamboo the 5 bigger pandas eat in a week
    bigger_pandas_weekly_bamboo = 5 * 40 * 7

    # Calculate the total amount of bamboo the 9 pandas eat in a week
    total_weekly_bamboo = small_pandas_weekly_bamboo + bigger_pandas_weekly_bamboo

    # Display the total amount of bamboo the 9 pandas eat in a week
    result = total_weekly_bamboo
    return result

print(solution())