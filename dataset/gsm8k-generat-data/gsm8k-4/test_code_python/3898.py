def solution():
    """Susie opens a pizza store. She charges $3 per slice and $15 for a whole pizza. If she was able to sell 24 slices of pizza and 3 whole pizzas, how much money did she earn?"""
    # Define the prices of slices and whole pizzas
    slice_price = 3
    pizza_price = 15

    # Calculate the earnings from selling slices
    slice_earnings = slice_price * 24

    # Calculate the earnings from selling whole pizzas
    pizza_earnings = pizza_price * 3

    # Calculate the total earnings
    total_earnings = slice_earnings + pizza_earnings

    # return the result
    result = total_earnings
    return result

print(solution())