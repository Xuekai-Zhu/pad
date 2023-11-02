def solution():
    """A certain store sells computer accessories and equipment. Due to a fire outbreak in one of the factories, the price of RAM increased by 30%. After two years, the price stabilized and finally fell by 20% from what it has risen. What is the current price of RAM if it was $50 before the fire?"""
    
    initial_price = 50
    fire_increase = initial_price * 0.3
    fire_price = initial_price + fire_increase
    stabilized_price = fire_price * (1 - 0.2)
    result = stabilized_price
    
    return result

print(solution())