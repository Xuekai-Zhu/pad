def solution():
     Reggie_layups = 3
     Reggie_free_throws = 2
     Reggie_long_shots = 1
     Reggie_points = Reggie_layups + (Reggie_free_throws * 2) + (Reggie_long_shots * 3)
     
     brother_long_shots = 4
     brother_points = brother_long_shots * 3
     
     Reggie_loss = brother_points - Reggie_points
     result = Reggie_loss
     return result

print(solution())