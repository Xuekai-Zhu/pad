def solution():
    # Define the daily average sales
    pastry_avg = 20
    bread_avg = 10

    # Calculate the total sales for today
    pastry_today = 14
    bread_today = 25

    total_today = pastry_today * 2 + bread_today * 4

    # Calculate the daily average sales
    total_avg = pastry_avg * 2 + bread_avg * 4

    # Calculate the difference between today's sales and the daily average
    difference = total_avg - total_today

    result = difference
    return result

print(solution())