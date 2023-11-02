def solution():
    bikes_sold_friday = 10
    bikes_bought_friday = 15
    bikes_sold_saturday = 12
    bikes_bought_saturday = 8
    bikes_sold_sunday = 9
    bikes_bought_sunday = 11
    
    total_bikes_bought = bikes_bought_friday + bikes_bought_saturday + bikes_bought_sunday
    total_bikes_sold = bikes_sold_friday + bikes_sold_saturday + bikes_sold_sunday
    
    net_increase = total_bikes_bought - total_bikes_sold
    
    result = net_increase
    
    return result

print(solution())