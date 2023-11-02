def solution():
    # Calculate the total profit John would make producing 1000 tires a day
    tire_production = 1000
    tire_cost = 250
    tire_sale = 1.5 * tire_cost
    daily_profit = tire_production * (tire_sale - tire_cost)

    # Calculate the profit John would make selling an additional 200 tires a day
    additional_production = 200
    additional_profit = additional_production * (tire_sale - tire_cost)

    # Calculate the weekly profit John is missing out on by not producing 1200 tires a day
    weekly_profit_lost = 5 * (1200 - tire_production) * (tire_sale - tire_cost)

    # Calculate the total profit John is making
    total_profit = 7 * daily_profit

    # Calculate John's net lost
    net_lost = weekly_profit_lost - additional_profit
    result = net_lost

    return result

print(solution())