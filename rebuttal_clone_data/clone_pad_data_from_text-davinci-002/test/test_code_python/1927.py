def solution():
    total_flour = 6
    cake_flour = 4
    cakes_made = cake_flour / 0.5
    cupcake_flour = total_flour - cake_flour
    cupcakes_made = cupcake_flour / 0.2
    cake_price = 2.5
    cupcake_price = 1
    total_sale = (cakes_made * cake_price) + (cupcakes_made * cupcake_price)
    result = total_sale
    
    return result

print(solution())