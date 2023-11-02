def solution():
    flour_available = 6
    flour_for_cakes = 4
    flour_for_cupcakes = 2
    cake_flour_per_piece = 0.5
    cupcake_flour_per_piece = 1/5
    cake_price = 2.5
    cupcake_price = 1

    # Calculate the number of cakes Gary can make
    num_cakes = flour_for_cakes / cake_flour_per_piece

    # Calculate the number of cupcakes Gary can make
    num_cupcakes = flour_for_cupcakes / cupcake_flour_per_piece

    # Calculate the total earnings from selling the cakes and cupcakes
    total_earnings = (num_cakes * cake_price) + (num_cupcakes * cupcake_price)
    result = total_earnings
    return result

print(solution())