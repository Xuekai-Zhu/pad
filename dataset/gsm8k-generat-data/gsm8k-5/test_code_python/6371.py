def solution():
    cash_register_cost = 1040  # Cost of new cash register
    bread_sold_per_day = 40  # Number of loaves sold per day
    bread_price = 2  # Price of each loaf of bread
    cakes_sold_per_day = 6  # Number of cakes sold per day
    cake_price = 12  # Price of each cake
    rent_per_day = 20  # Cost of rent per day
    electricity_per_day = 2  # Cost of electricity per day
    
    # Calculate the daily profit
    daily_profit = (bread_sold_per_day * bread_price) + (cakes_sold_per_day * cake_price) - rent_per_day - electricity_per_day
    
    # Calculate the number of days needed to pay for the cash register
    days_needed = cash_register_cost / daily_profit
    result = days_needed
    return result

print(solution())