def solution():
    
    washing_machine_price = 100
    dryer_price = washing_machine_price - 30
    total_price = washing_machine_price + dryer_price
    discount = total_price * 0.1
    discounted_price = total_price - discount
    result = discounted_price
    return result

print(solution())