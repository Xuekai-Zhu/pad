def solution():
    """The price of buying a wooden toy at the new Craftee And Best store is $20, and the cost of buying a hat is $10. If Kendra went to the shop with a $100 bill and bought two wooden toys and three hats, calculate the change she received."""
    # Define the prices of the wooden toy and hat
    TOY_PRICE = 20
    HAT_PRICE = 10

    # Define the number of wooden toys and hats Kendra bought
    num_toys = 2
    num_hats = 3

    # Calculate the total cost
    total_cost = (TOY_PRICE * num_toys) + (HAT_PRICE * num_hats)

    # Calculate the change Kendra received
    change = 100 - total_cost

    # Display the change
    result = change
    return result

print(solution())