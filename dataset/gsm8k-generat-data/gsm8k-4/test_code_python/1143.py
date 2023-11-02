def solution():
    """The price of buying a wooden toy at the new Craftee And Best store is $20, and the cost of buying a hat is $10. If Kendra went to the shop with a $100 bill and bought two wooden toys and three hats, calculate the change she received."""
    # Define the prices of wooden toys and hats
    wooden_toy_price = 20
    hat_price = 10

    # Define the number of wooden toys and hats purchased
    wooden_toys_purchased = 2
    hats_purchased = 3

    # Calculate the total cost of the purchase
    total_cost = (wooden_toy_price * wooden_toys_purchased) + (hat_price * hats_purchased)

    # Calculate the amount of change
    change = 100 - total_cost

    # Return the result
    result = change
    return result

print(solution())