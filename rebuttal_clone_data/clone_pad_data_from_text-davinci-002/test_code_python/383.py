def solution():
     cupcakes_baked = 60
     cupcakes_given_away = cupcakes_baked * (4/5)
     cupcakes_eaten = cupcakes_baked * (1/5) * (3/1)
     cupcakes_left = cupcakes_baked - cupcakes_given_away - cupcakes_eaten
     result = cupcakes_left
     return result

print(solution())