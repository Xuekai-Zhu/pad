def solution():
    
    pasta_order = 2
    bbq_order = 3
    dinner_order = 8
    num_pasta_orders = 6
    num_bbq_orders = 3
    num_dinner_orders = 2
    
    total_pasta = pasta_order * num_pasta_orders
    total_bbq = bbq_order * num_bbq_orders
    total_dinner = dinner_order * num_dinner_orders
    
    total_chicken = total_pasta + total_bbq + total_dinner
    result = total_chicken
    
    return result

print(solution())