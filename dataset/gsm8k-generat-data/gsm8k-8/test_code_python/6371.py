def solution():
    register_cost = 1040
    bread_sold_per_day = 40
    bread_price = 2
    cakes_sold_per_day = 6
    cake_price = 12
    rent_per_day = 20
    electricity_per_day = 2

    # Calculate the daily profit
    daily_profit = (bread_sold_per_day * bread_price) + (cakes_sold_per_day * cake_price) - \
                   (rent_per_day + electricity_per_day)

    # Calculate the number of days needed to pay for the cash register
    days_to_pay_for_register = register_cost / daily_profit
    result = days_to_pay_for_register
    return result

print(solution())