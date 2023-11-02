def solution():
    """Anna used four baking trays to bake cupcakes. Each tray has 20 cupcakes and each cupcake was then sold for $2.
    If only 3/5 of the cupcakes were sold and the rest were kept, how much did Anna earn from it?"""
    trays_baked = 4
    cupcakes_per_tray = 20
    total_cupcakes = trays_baked * cupcakes_per_tray
    sold_cupcakes = total_cupcakes * (3/5)
    remaining_cupcakes = total_cupcakes - sold_cupcakes
    price_per_cupcake = 2
    total_earnings = sold_cupcakes * price_per_cupcake
    result = total_earnings
    return result

print(solution())