def solution():
    """Chandler can eat a total of 23 apples and Lucy can eat a total of 19 apples per week. If the farmer only delivers 1 time per month, how many apples do they have to order for a month?"""
    # Calculate the total number of apples Chandler and Lucy can eat in a week
    weekly_total = 23 + 19

    # Calculate the total number of apples they need for a month (assuming 4 weeks in a month)
    monthly_total = weekly_total * 4

    # Display the total number of apples needed for a month
    result = monthly_total
    return result

print(solution())