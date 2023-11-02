def solution():
    num_trays = 4
    cupcakes_per_tray = 20
    price_per_cupcake = 2
    sold_ratio = 3/5

    # Calculate the total number of cupcakes baked
    total_cupcakes = num_trays * cupcakes_per_tray

    # Calculate the number of cupcakes sold
    num_sold_cupcakes = total_cupcakes * sold_ratio

    # Calculate the total earnings from the sold cupcakes
    total_earnings = num_sold_cupcakes * price_per_cupcake
    result = total_earnings
    return result

print(solution())