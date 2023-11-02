def solution():
    
    friday_sold = 10
    friday_bought = 15
    saturday_sold = 12
    saturday_bought = 8
    sunday_sold = 9
    sunday_bought = 11
    total_sold = friday_sold + saturday_sold + sunday_sold
    total_bought = friday_bought + saturday_bought + sunday_bought
    net_increase = total_bought - total_sold
    result = net_increase
    return result

print(solution())