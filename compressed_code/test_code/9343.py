def solution():
    
    banana_cost = 1
    apple_cost = 2
    strawberry_cost = (4/12)
    avocado_cost = 3
    grapes_cost_per_bunch = 4
    
    num_bananas = 4
    num_apples = 3
    num_strawberries = 24
    num_avocados = 2
    num_grapes = 1
    
    total_cost = (num_bananas*banana_cost) + (num_apples*apple_cost) + (num_strawberries*strawberry_cost) + (num_avocados*avocado_cost) + (num_grapes*grapes_cost_per_bunch)
    result = total_cost
    return result

print(solution())