def solution():
    
    cupcakes = 5
    donuts = 6
    apple_pie_slices = 4
    cookies = 15
    price_cupcake = 2
    price_donut = 1
    price_apple_pie_slice = 2
    price_cookie = 0.60
    
    total_cost = (cupcakes * price_cupcake) + (donuts * price_donut) + (apple_pie_slices * price_apple_pie_slice) + (cookies * price_cookie)
    result = total_cost
    return result

print(solution())