def solution():
    """Jane sews 2 dresses a day for 7 days. Then she sews 3 dresses a day for the next 2 days. In the end, she adds 2 ribbons to each dress. How many ribbons does Jane use in total?"""
    # Define the number of dresses Jane sews each day
    dresses_per_day_1 = 2
    dresses_per_day_2 = 3

    # Define the number of days Jane sews
    days_1 = 7
    days_2 = 2

    # Calculate the total number of dresses that Jane sews
    total_dresses = (dresses_per_day_1 * days_1) + (dresses_per_day_2 * days_2)

    # Calculate the total number of ribbons used
    ribbons_per_dress = 2
    total_ribbons = total_dresses * ribbons_per_dress

    # Display the total number of ribbons
    result = total_ribbons
    return result

print(solution())