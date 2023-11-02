def solution():
    
    
    initial_price = 50
    fire_increase = initial_price * 0.3
    fire_price = initial_price + fire_increase
    stabilized_price = fire_price * (1 - 0.2)
    result = stabilized_price
    
    return result

print(solution())