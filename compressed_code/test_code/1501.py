def solution():
    
    friday_start = 0
    friday_sold = 10
    friday_fixed = 15
    friday_end = friday_start + friday_fixed - friday_sold
    saturday_start = friday_end
    saturday_sold = 12
    saturday_fixed = 8
    saturday_end = saturday_start + saturday_fixed - saturday_sold
    sunday_start = saturday_end
    sunday_sold = 9
    sunday_fixed = 11
    sunday_end = sunday_start + sunday_fixed - sunday_sold
    net_increase = sunday_end - friday_start
    result = net_increase
    return result

print(solution())