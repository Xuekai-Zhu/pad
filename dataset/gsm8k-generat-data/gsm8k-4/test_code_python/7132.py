def solution():
    """Anna used four baking trays to bake cupcakes. Each tray has 20 cupcakes and each cupcake was then sold for $2. If only 3/5 of the cupcakes were sold and the rest were kept, how much did Anna earn from it?"""
    # Define the number of baking trays and cupcakes per tray
    trays = 4
    cupcakes_per_tray = 20

    # Calculate the total number of cupcakes baked
    total_cupcakes = trays * cupcakes_per_tray

    # Calculate the number of cupcakes sold and kept
    cupcakes_sold = total_cupcakes * 3/5
    cupcakes_kept = total_cupcakes * 2/5

    # Calculate the earnings from sold cupcakes
    earnings = cupcakes_sold * 2

    # Return the result
    result = earnings
    return result

print(solution())