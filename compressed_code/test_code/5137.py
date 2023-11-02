def solution():
    
    home_sugar = 3
    store_sugar = 2 * 6
    total_sugar = home_sugar + store_sugar
    batter_sugar_per_dozen = 1
    frosting_sugar_per_dozen = 2
    sugar_per_dozen = batter_sugar_per_dozen + frosting_sugar_per_dozen
    dozen_cupcakes = total_sugar // sugar_per_dozen
    result = dozen_cupcakes
    return result

print(solution())