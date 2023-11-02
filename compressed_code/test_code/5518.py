def solution():
    
    num_trays = 4
    cupcakes_per_tray = 20
    total_cupcakes = num_trays * cupcakes_per_tray
    sold_cupcakes = total_cupcakes * (3/5)
    kept_cupcakes = total_cupcakes - sold_cupcakes
    earnings = sold_cupcakes * 2
    result = earnings
    return result

print(solution())