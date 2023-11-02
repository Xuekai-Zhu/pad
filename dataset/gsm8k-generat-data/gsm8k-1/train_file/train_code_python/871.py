def solution():
    """John decided to buy 10 pins for himself. They are normally $20 each but they were on sale for 15% off. How much did he spend on pins?"""
    num_pins = 10
    pin_price = 20
    percent_off = 15
    discounted_price = pin_price - (pin_price * (percent_off / 100))
    total_cost = num_pins * discounted_price
    result = total_cost
    return result

print(solution())