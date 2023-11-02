def solution():
    # Calculate the number of bottles sold by Nick
    nick_sales = 55 - 6  

    # Calculate the total sales in the morning
    morning_sales = 55 * 0.50  

    # Calculate the total sales in the evening
    evening_sales = (55 + nick_sales) * 0.50  

    # Calculate the difference in earnings between evening and morning sales
    earnings_difference = evening_sales - morning_sales 

    result = earnings_difference
    return result

print(solution())