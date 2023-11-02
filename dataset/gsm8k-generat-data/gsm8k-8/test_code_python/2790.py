def solution():
    # Calculate the total amount of bamboo eaten by the small pandas in a week
    small_pandas_weekly_bamboo = 4 * 25 * 7

    # Calculate the total amount of bamboo eaten by the bigger pandas in a week
    big_pandas_weekly_bamboo = 5 * 40 * 7

    # Calculate the total amount of bamboo eaten by all 9 pandas in a week
    total_weekly_bamboo = small_pandas_weekly_bamboo + big_pandas_weekly_bamboo

    result = total_weekly_bamboo
    return result

print(solution())