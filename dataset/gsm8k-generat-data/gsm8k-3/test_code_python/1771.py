def solution():
    """Sophie buys five cupcakes at $2 each,  six doughnuts at $1 each,  four slices of apple pie at $2 per slice, and fifteen cookies at $0.60 each. How much does she spend in all?"""
    # Define the prices of each item
    CUPCAKE_PRICE = 2
    DONUT_PRICE = 1
    PIE_PRICE = 2
    COOKIE_PRICE = 0.6

    # Define the quantities of each item purchased
    num_cupcakes = 5
    num_donuts = 6
    num_pie_slices = 4
    num_cookies = 15

    # Calculate the total cost
    total_cost = (num_cupcakes * CUPCAKE_PRICE) + (num_donuts * DONUT_PRICE) + (num_pie_slices * PIE_PRICE) + (num_cookies * COOKIE_PRICE)

    # Display the total cost
    result = total_cost
    return result

print(solution())