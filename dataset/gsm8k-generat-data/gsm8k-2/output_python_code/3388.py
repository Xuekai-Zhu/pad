def solution():
    """A certain store sells computer accessories and equipment. Due to a fire outbreak in one of the factories, the price of RAM increased by 30%. After two years, the price stabilized and finally fell by 20% from what it has risen. What is the current price of RAM if it was $50 before the fire?"""
    initial_price = 50
    fire_increase = 0.3
    after_fire_price = initial_price + (initial_price * fire_increase)
    stabilization_time = 2
    post_stabilization_drop = 0.2
    final_price = after_fire_price - (after_fire_price * post_stabilization_drop)
    result = final_price
    return result

print(solution())