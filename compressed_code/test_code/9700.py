def solution():
    
    price_per_bottle = 20.00
    tariff_increase = 0.25
    new_price_per_bottle = price_per_bottle + (price_per_bottle * tariff_increase)
    num_bottles = 5
    total_increase = (new_price_per_bottle - price_per_bottle) * num_bottles
    result = total_increase
    return result

print(solution())