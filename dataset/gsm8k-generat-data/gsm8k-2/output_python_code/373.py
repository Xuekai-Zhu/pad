def solution():
    """There are 40 more buyers in the grocery store today than yesterday. There were half the number of buyers yesterday as there were the day before, and the day before had 50 buyers. Nobody visited the store on more than one day. What's the total number of buyers who've visited the store in the three days?"""
    day_before_yesterday_buyers = 50
    yesterday_buyers = day_before_yesterday_buyers / 2
    today_buyers = yesterday_buyers + 40
    total_buyers = day_before_yesterday_buyers + yesterday_buyers + today_buyers
    result = total_buyers
    return result

print(solution())