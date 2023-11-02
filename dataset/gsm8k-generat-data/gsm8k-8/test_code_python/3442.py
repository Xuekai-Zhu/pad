def solution():
    # Calculate the number of cakes Gary can make
    cakes_flour = 4
    cake_flour_needed = 0.5
    num_cakes = cakes_flour / cake_flour_needed

    # Calculate the number of cupcakes Gary can make
    cupcakes_flour = 2
    cupcake_flour_needed = 1/5
    num_cupcakes = cupcakes_flour / cupcake_flour_needed

    # Calculate the total earnings from the cakes and cupcakes
    cake_earnings = num_cakes * 2.5
    cupcake_earnings = num_cupcakes * 1
    total_earnings = cake_earnings + cupcake_earnings

    result = total_earnings
    return result

print(solution())