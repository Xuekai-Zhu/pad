def solution():
    """Anna used four baking trays to bake cupcakes. Each tray has 20 cupcakes and each cupcake was then sold for $2. If only 3/5 of the cupcakes were sold and the rest were kept, how much did Anna earn from it?"""
    # Define the number of baking trays and cupcakes per tray
    TRAYS = 4
    CUPCAKES_PER_TRAY = 20

    # Calculate the total number of cupcakes baked
    total_cupcakes = TRAYS * CUPCAKES_PER_TRAY

    # Calculate the number of cupcakes sold and kept
    sold_cupcakes = total_cupcakes * (3 / 5)
    kept_cupcakes = total_cupcakes - sold_cupcakes

    # Calculate Anna's earnings from the sold cupcakes
    earnings = sold_cupcakes * 2

    # Display Anna's earnings
    result = earnings
    return result

print(solution())