def solution():
    
    total_watermelons = 10 * 12  
    yesterday_sold = total_watermelons * 0.4
    remaining_watermelons = total_watermelons - yesterday_sold
    today_sold = remaining_watermelons / 4
    left_to_sell = remaining_watermelons - today_sold
    result = left_to_sell
    return result

print(solution())