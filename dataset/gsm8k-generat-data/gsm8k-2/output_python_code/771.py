def solution():
    """Kylie picks apples for 3 hours. The first hour she picks 66 apples. The second hour she doubles her apple picking rate, and the third hour she picks a third of the apples picked in the first hour. How many apples did Kylie pick total?"""
    first_hour_apples = 66
    second_hour_apples = 2 * first_hour_apples
    third_hour_apples = first_hour_apples / 3
    total_apples = first_hour_apples + second_hour_apples + third_hour_apples
    result = total_apples
    return result

print(solution())