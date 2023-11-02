def solution():
    
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