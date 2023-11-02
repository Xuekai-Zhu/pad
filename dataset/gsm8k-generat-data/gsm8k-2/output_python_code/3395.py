def solution():
    """Remy sold 55 bottles of soda in the morning. Nick sold six fewer bottles of soda than Remy. The price per bottle is $.50. If their total evening sales are $55, how much more did they earn in the evening than in the morning?"""
    remy_morning_sales = 55
    nick_morning_sales = remy_morning_sales - 6
    total_morning_sales = remy_morning_sales + nick_morning_sales
    
    evening_sales = 55
    total_sales = evening_sales / 0.5 #total number of bottles sold in the evening
    
    morning_sales = total_sales - evening_sales #total number of bottles sold in the morning
    
    morning_earnings = morning_sales * 0.5
    evening_earnings = evening_sales * 0.5
    
    difference = evening_earnings - morning_earnings
    
    result = difference
    return result

print(solution())