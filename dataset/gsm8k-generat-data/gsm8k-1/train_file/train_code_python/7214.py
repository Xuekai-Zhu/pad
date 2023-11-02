def solution():
    """A baker is comparing the day’s sales to his daily average. He usually sells 20 pastries and 10 loaves of bread. Today, he sells 14 pastries and 25 loaves of bread. If pastries are sold for $2 and loaves of bread are sold for $4, what is the difference, in dollars, between the baker’s daily average and total for today?"""
    pastries_daily_average = 20
    loaves_daily_average = 10
    pastries_sold_today = 14
    loaves_sold_today = 25
    pastry_price = 2
    loaf_price = 4

    daily_average_total = (pastries_daily_average * pastry_price) + (loaves_daily_average * loaf_price)
    today_total = (pastries_sold_today * pastry_price) + (loaves_sold_today * loaf_price)

    difference = today_total - daily_average_total
    result = difference

    return result

print(solution())