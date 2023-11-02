def solution():
    """A baker is comparing the day’s sales to his daily average. He usually sells 20 pastries and 10 loaves of bread. Today, he sells 14 pastries and 25 loaves of bread. If pastries are sold for $2 and loaves of bread are sold for $4, what is the difference, in dollars, between the baker’s daily average and total for today?"""
    # Define the price of pastries and loaves of bread
    pastry_price = 2
    bread_price = 4

    # Define the daily average sales and today's sales
    daily_avg_sales = (20 * pastry_price) + (10 * bread_price)
    today_sales = (14 * pastry_price) + (25 * bread_price)

    # Calculate the difference between daily average and today's sales
    difference = today_sales - daily_avg_sales

    result = difference
    return result

print(solution())