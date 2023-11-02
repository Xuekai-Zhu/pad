def solution():
    
    initial_price = 50
    fire_increase = 0.3
    after_fire_price = initial_price + (initial_price * fire_increase)
    stabilization_time = 2
    post_stabilization_drop = 0.2
    final_price = after_fire_price - (after_fire_price * post_stabilization_drop)
    result = final_price
    return result

print(solution())