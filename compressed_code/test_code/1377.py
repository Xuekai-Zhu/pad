def solution():
    
    cupcakes = 5
    cupcakes_price = 2
    doughnuts = 6
    doughnuts_price = 1
    apple_pie_slices = 4
    apple_pie_slice_price = 2
    cookies = 15
    cookies_price = 0.60

    total_cost = (cupcakes * cupcakes_price) + (doughnuts * doughnuts_price) + (apple_pie_slices * apple_pie_slice_price) + (cookies * cookies_price)

    result = total_cost
    return result

print(solution())