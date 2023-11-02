def solution():
    
    # Define the initial price of the grocery store
    initial_price = 120

    # Calculate the new price of the grocery store after 3 years
    new_price = initial_price + (initial_price * 0.05)

    # Round the price to the nearest integer
    rounded_price = round(new_price)

    # Display the rounded price
    result = rounded_price
    return result

print(solution())