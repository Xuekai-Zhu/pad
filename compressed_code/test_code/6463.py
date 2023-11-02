def solution():
    
    num_pins = 10
    pin_price = 20
    percent_off = 15
    discounted_price = pin_price - (pin_price * (percent_off / 100))
    total_cost = num_pins * discounted_price
    result = total_cost
    return result

print(solution())