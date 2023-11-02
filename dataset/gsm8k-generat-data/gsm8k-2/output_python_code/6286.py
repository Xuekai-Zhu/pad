def solution():
    """John can produce 1000 tires a day. It costs $250 to produce each tire. He manages to sell them for 1.5 times as much. He could sell 1200 tires a day if his factory was able to produce more. How much money does he lose out on a week by not being able to produce all the tires?"""
    daily_production = 1000
    production_cost = 250
    selling_price = 1.5 * production_cost
    daily_profit = selling_price - production_cost
    lost_daily_sales = 1200 - daily_production
    lost_daily_profit = lost_daily_sales * daily_profit
    lost_weekly_profit = 7 * lost_daily_profit
    
    result = lost_weekly_profit
    
    return result

print(solution())