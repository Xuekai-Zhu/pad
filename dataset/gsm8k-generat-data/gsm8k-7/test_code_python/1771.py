def solution():
    num_cupcakes = 5
    cupcakes_price = 2

    num_doughnuts = 6
    doughnuts_price = 1

    num_apple_pie_slices = 4
    apple_pie_price_per_slice = 2

    num_cookies = 15
    cookies_price_each = 0.60

    # Calculate the total cost of all cupcakes
    total_cupcakes_cost = num_cupcakes * cupcakes_price

    # Calculate the total cost of all doughnuts
    total_doughnuts_cost = num_doughnuts * doughnuts_price

    # Calculate the total cost of all slices of apple pie
    total_apple_pie_cost = num_apple_pie_slices * apple_pie_price_per_slice

    # Calculate the total cost of all cookies
    total_cookies_cost = num_cookies * cookies_price_each

    # Calculate the total cost of all items
    total_cost = total_cupcakes_cost + total_doughnuts_cost + total_apple_pie_cost + total_cookies_cost
    result = total_cost
    return result

print(solution())