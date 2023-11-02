def solution():
    
    regular_price = 25.00
    sale_price = 20.00
    bottles = 2
    loads_per_bottle = 80
    regular_price_per_load = regular_price / loads_per_bottle
    sale_price_per_load = (sale_price * bottles) / (loads_per_bottle * bottles)
    result = int(sale_price_per_load * 100)
    return result

print(solution())