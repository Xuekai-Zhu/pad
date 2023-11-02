def solution():
     recipes = 3
     soy_sauce_per_recipe = [2, 1, 3]
     soy_sauce_needed = sum(soy_sauce_per_recipe)
     soy_sauce_total = soy_sauce_needed * 16
     result = soy_sauce_total / 128
     return result

print(solution())