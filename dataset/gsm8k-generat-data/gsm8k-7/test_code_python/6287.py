def solution():
    production_per_day = 1000
    cost_per_tire = 250
    selling_price_per_tire = 1.5 * cost_per_tire
    max_production_per_day = 1200
    num_days_per_week = 7

    # Calculate the revenue from selling all the tires he can produce
    revenue_from_max_production = max_production_per_day * selling_price_per_tire

    # Calculate the cost of producing all the tires he can produce
    cost_of_max_production = max_production_per_day * cost_per_tire

    # Calculate the revenue from selling all the tires he currently produces
    revenue_from_current_production = production_per_day * selling_price_per_tire

    # Calculate the cost of producing all the tires he currently produces
    cost_of_current_production = production_per_day * cost_per_tire

    # Calculate the total profit from selling all the tires he currently produces
    profit_from_current_production = revenue_from_current_production - cost_of_current_production

    # Calculate the total profit from selling all the tires he could produce
    profit_from_max_production = revenue_from_max_production - cost_of_max_production

    # Calculate the difference in profit between current and max production
    lost_profit_per_week = (profit_from_max_production - profit_from_current_production) * num_days_per_week
    result = lost_profit_per_week
    return result

print(solution())