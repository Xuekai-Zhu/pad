def solution():
    stock_on_friday = 0
    bikes_sold_friday = 10
    bikes_bought_friday = 15
    bikes_sold_sat = 12
    bikes_bought_sat = 8
    bikes_sold_sun = 9
    bikes_bought_sun = 11

    # Calculate the net increase in stock on Friday
    stock_on_friday += bikes_bought_friday
    stock_on_friday -= bikes_sold_friday

    # Calculate the net increase in stock on Saturday
    stock_on_saturday = stock_on_friday + bikes_bought_sat
    stock_on_saturday -= bikes_sold_sat

    # Calculate the net increase in stock on Sunday
    stock_on_sunday = stock_on_saturday + bikes_bought_sun
    stock_on_sunday -= bikes_sold_sun

    # Calculate the net increase in stock over the three days
    net_increase = stock_on_sunday - stock_on_friday

    result = net_increase
    return result

print(solution())