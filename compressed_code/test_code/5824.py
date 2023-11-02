def solution():
    
    ice_cream_cost = 4
    frozen_yoghurt_cost = 1
    ice_cream_cartons = 10
    frozen_yoghurt_cartons = 4
    total_ice_cream_cost = ice_cream_cost * ice_cream_cartons
    total_frozen_yoghurt_cost = frozen_yoghurt_cost * frozen_yoghurt_cartons
    difference = total_ice_cream_cost - total_frozen_yoghurt_cost
    result = difference
    return result

print(solution())