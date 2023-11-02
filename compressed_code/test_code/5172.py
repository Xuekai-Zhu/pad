def solution():
    
    gas_station_price = 1.75
    amazon_price_per_lighter = 5 / 12
    amazon_price_for_24 = 24 * amazon_price_per_lighter
    gas_station_price_for_24 = 24 * gas_station_price
    savings = gas_station_price_for_24 - amazon_price_for_24
    result = savings
    return result

print(solution())