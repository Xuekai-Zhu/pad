def solution():
    
    total_cartons_needed = 42
    strawberries_in_cupboard = 2
    blueberries_in_cupboard = 7
    cartons_in_cupboard = strawberries_in_cupboard + blueberries_in_cupboard
    cartons_to_buy = total_cartons_needed - cartons_in_cupboard
    result = cartons_to_buy
    return result

print(solution())