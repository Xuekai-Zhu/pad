def solution():
    """Anna used four baking trays to bake cupcakes. Each tray has 20 cupcakes and each cupcake was then sold for $2. If only 3/5 of the cupcakes were sold and the rest were kept, how much did Anna earn from it?"""
    num_trays = 4
    cupcakes_per_tray = 20
    total_cupcakes = num_trays * cupcakes_per_tray
    sold_cupcakes = total_cupcakes * (3/5)
    kept_cupcakes = total_cupcakes - sold_cupcakes
    earnings = sold_cupcakes * 2
    result = earnings
    return result

print(solution())