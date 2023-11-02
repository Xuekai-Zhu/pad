def solution():
    """A baker sells pastries for $5 and works 7 days a week. On Monday he sold 2. Every day the number of sales increases by 1 compared to the previous day. On average, how many pastries does he sell on each day of the week?"""
    # Define the initial number of pastries sold on Monday and the daily increase
    monday_sales = 2
    daily_increase = 1

    # Calculate the total number of pastries sold in a week
    total_sales = monday_sales
    for i in range(6):
        total_sales += monday_sales + (i+1) * daily_increase

    # Calculate the average number of pastries sold per day
    avg_sales = total_sales / 7

    # return the result
    result = avg_sales
    return result

print(solution())