def solution():
    """Mark collects money for the homeless. He visits 20 households a day for 5 days and half of those households give him a pair of 20s. How much did he collect?"""
    # Define the number of households visited per day and the number of days
    households_per_day = 20
    num_days = 5

    # Calculate the total number of households visited
    total_households = households_per_day * num_days

    # Calculate the number of households that gave Mark money
    households_with_money = total_households / 2

    # Calculate the total amount of money collected
    total_money = households_with_money * 2 * 20

    # return the result
    result = round(total_money)
    return result

print(solution())