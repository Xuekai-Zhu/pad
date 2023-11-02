def solution():
    
    lemon_juice_per_cupcake = 1
    tablespoons_per_lemon = 4
    cupcakes_needed = 3 * 12
    lemons_needed = (cupcakes_needed * lemon_juice_per_cupcake) / tablespoons_per_lemon
    result = lemons_needed
    return result

print(solution())