def solution():
    
    land_size = 200
    buying_price_per_acre = 70
    total_buying_price = land_size * buying_price_per_acre
    selling_price_per_acre = 200
    half_land_size = land_size / 2
    total_selling_price = half_land_size * selling_price_per_acre
    profit = total_selling_price - total_buying_price
    result = profit
    return result

print(solution())