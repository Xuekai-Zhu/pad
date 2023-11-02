def solution():
    
    num_members = 20
    candy_price = 0.5
    avg_candy_bars_per_member = 8
    total_candy_bars_sold = num_members * avg_candy_bars_per_member
    total_earnings = total_candy_bars_sold * candy_price
    result = total_earnings
    return result

print(solution())