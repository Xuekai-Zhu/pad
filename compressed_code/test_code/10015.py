def solution():
    
    total_sales = 50
    winter_melon_sales = 2/5 * total_sales
    okinawa_sales = 3/10 * total_sales
    chocolate_sales = total_sales - winter_melon_sales - okinawa_sales
    result = chocolate_sales
    return result

print(solution())