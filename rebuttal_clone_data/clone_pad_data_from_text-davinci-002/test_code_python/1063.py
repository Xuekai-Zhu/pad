def solution():
     total_sugar = 720
     cake_layers = 2
     cupcakes = 12
     sugar_per_layer = total_sugar / cake_layers
     sugar_per_cupcake = sugar_per_layer / cupcakes
     result = sugar_per_cupcake
     return result

print(solution())