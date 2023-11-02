def solution():
    slices_sold = 24
    whole_pizzas_sold = 3

    # Calculate the total earnings from selling slices
    slice_price = 3
    slice_earnings = slices_sold * slice_price

    # Calculate the total earnings from selling whole pizzas
    pizza_price = 15
    pizza_earnings = whole_pizzas_sold * pizza_price

    # Calculate the total earnings
    total_earnings = slice_earnings + pizza_earnings
    result = total_earnings
    return result

print(solution())