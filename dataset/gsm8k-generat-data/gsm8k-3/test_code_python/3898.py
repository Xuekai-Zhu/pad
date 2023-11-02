def solution():
    """Susie opens a pizza store. She charges $3 per slice and $15 for a whole pizza. If she was able to sell 24 slices of pizza and 3 whole pizzas, how much money did she earn?"""
    # Define the price of a slice and a whole pizza
    SLICE_PRICE = 3
    PIZZA_PRICE = 15

    # Define the number of slices and whole pizzas sold
    slices_sold = 24
    pizzas_sold = 3

    # Calculate the total earnings from the slices sold
    slice_earnings = slices_sold * SLICE_PRICE

    # Calculate the total earnings from the whole pizzas sold
    pizza_earnings = pizzas_sold * PIZZA_PRICE

    # Calculate the total earnings
    total_earnings = slice_earnings + pizza_earnings

    # Display the total earnings
    result = total_earnings
    return result

print(solution())