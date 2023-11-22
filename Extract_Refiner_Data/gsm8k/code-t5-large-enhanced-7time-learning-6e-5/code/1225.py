def solution():
    
    # Define the initial price of the toy
    initial_price = 40

    # Calculate the price after the increase in December
    decrease_dec = initial_price * 0.8
    price_after_dece = initial_price + decrease_dec

    # Calculate the price after the decrease in January
    decrease_jan = price_after_dece * 0.5
    price_after_jan = price_after_dece - decrease_jan

    # Display the price after the decrease in January
    result = price_after_jan
    return result

print(solution())