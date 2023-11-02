def solution():
    """Remy sold 55 bottles of soda in the morning. Nick sold six fewer bottles of soda than Remy. The price per bottle is $.50. If their total evening sales are $55, how much more did they earn in the evening than in the morning?"""
    # Define the number of bottles sold in the morning
    morning_sales = 55

    # Calculate the number of bottles sold by Nick
    nick_sales = morning_sales - 6

    # Calculate the total number of bottles sold
    total_sales = morning_sales + nick_sales

    # Calculate the total earnings from sales in the evening
    evening_earnings = 55

    # Calculate the earnings from sales in the morning
    morning_earnings = morning_sales * 0.5

    # Calculate the earnings from sales in the evening
    evening_earnings = evening_earnings - morning_earnings

    # Calculate the difference in earnings between morning and evening
    difference = evening_earnings - morning_earnings

    # return the result
    result = difference
    return result

print(solution())