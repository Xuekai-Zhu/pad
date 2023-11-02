def solution():
    loads_per_bottle = 80
    price_per_bottle = 2500
    sale_price = 2000
    bottles_bought = 2
    total_price = sale_price * bottles_bought
    total_loads = loads_per_bottle * bottles_bought
    price_per_load = total_price / total_loads
    result = price_per_load
    return result

print(solution())