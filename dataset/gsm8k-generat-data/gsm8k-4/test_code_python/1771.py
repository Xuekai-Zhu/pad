def solution():
    """Sophie buys five cupcakes at $2 each, six doughnuts at $1 each, four slices of apple pie at $2 per slice, and fifteen cookies at $0.60 each. How much does she spend in all?"""
    # Define the prices of the items
    cupcake_price = 2
    doughnut_price = 1
    apple_pie_price = 2
    cookie_price = 0.6

    # Calculate the total cost of cupcakes
    num_cupcakes = 5
    cupcakes_cost = num_cupcakes * cupcake_price

    # Calculate the total cost of doughnuts
    num_doughnuts = 6
    doughnuts_cost = num_doughnuts * doughnut_price

    # Calculate the total cost of apple pie
    num_slices_apple_pie = 4
    apple_pie_cost = num_slices_apple_pie * apple_pie_price

    # Calculate the total cost of cookies
    num_cookies = 15
    cookies_cost = num_cookies * cookie_price

    # Calculate the total cost of all items
    total_cost = cupcakes_cost + doughnuts_cost + apple_pie_cost + cookies_cost

    result = total_cost
    return result

print(solution())