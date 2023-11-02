def solution():
     lettuce = 50
     carrots = lettuce * 2
     dressing = 210
     crust = 600
     pepperoni = crust / 3
     cheese = 400
     salad = lettuce + carrots + dressing
     pizza = crust + pepperoni + cheese
     salad_portion = salad / 4
     pizza_portion = pizza / 5
     total_calories = salad_portion + pizza_portion
     result = total_calories
     return result

print(solution())