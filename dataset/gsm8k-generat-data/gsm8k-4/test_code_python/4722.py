def solution():
    """Jane sews 2 dresses a day for 7 days. Then she sews 3 dresses a day for the next 2 days. In the end, she adds 2 ribbons to each dress. How many ribbons does Jane use in total?"""
    # Define the number of days and dresses sewn each day
    days = 9
    dresses_per_day = [2] * 7 + [3] * 2

    # Calculate the total number of dresses sewn
    total_dresses = sum(dresses_per_day)

    # Calculate the total number of ribbons used
    total_ribbons = total_dresses * 2

    # return the result
    result = total_ribbons
    return result

print(solution())