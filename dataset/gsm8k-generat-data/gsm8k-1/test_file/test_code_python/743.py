def solution():
    """A tomato vendor decides to switch who he buys his tomatoes for. He sells 500 tomatoes a day. He used to buy them for $.5 each but he gets a new vendor who sells them for $.4 each. How much money does he save a week?"""
    tomatoes_per_day = 500
    old_price = 0.5
    new_price = 0.4
    daily_savings = (old_price - new_price) * tomatoes_per_day
    weekly_savings = daily_savings * 7
    result = weekly_savings
    return result

print(solution())