def solution():
     """Caleb bought 10 cartons of ice cream and 4 cartons of frozen yoghurt. Each carton of ice cream cost $4 and each carton of frozen yoghurt cost $1. How much more did Caleb spend on ice cream than on frozen yoghurt?"""
     ice_cream_cartons = 10
     frozen_yoghurt_cartons = 4
     price_ice_cream_carton = 4
     price_frozen_yoghurt_carton = 1
     total_spent_ice_cream = ice_cream_cartons * price_ice_cream_carton
     total_spent_frozen_yoghurt = frozen_yoghurt_cartons * price_frozen_yoghurt_carton
     difference = total_spent_ice_cream - total_spent_frozen_yoghurt
     result = difference
     return result

print(solution())