def solution():
    """Sophie buys five cupcakes at $2 each, six doughnuts at $1 each, four slices of apple pie at $2 per slice, and fifteen cookies at $0.60 each. How much does she spend in all?"""
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