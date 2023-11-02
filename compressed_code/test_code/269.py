def solution():
    
    day_before_yesterday_buyers = 50
    yesterday_buyers = day_before_yesterday_buyers / 2
    today_buyers = yesterday_buyers + 40
    total_buyers = day_before_yesterday_buyers + yesterday_buyers + today_buyers
    result = total_buyers
    return result

print(solution())