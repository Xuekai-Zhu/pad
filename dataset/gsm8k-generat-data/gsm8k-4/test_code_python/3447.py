def solution():
    """Chandler can eat a total of 23 apples and Lucy can eat a total of 19 apples per week. If the farmer only delivers 1 time per month, how many apples do they have to order for a month?"""
    # Define the number of apples Chandler and Lucy can eat in a week
    chandler_weekly = 23
    lucy_weekly = 19

    # Calculate the total number of apples they can eat in a month
    total_weekly = chandler_weekly + lucy_weekly
    total_monthly = total_weekly * 4

    # return the result
    result = total_monthly
    return result

print(solution())