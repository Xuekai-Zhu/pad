def solution():
    """Vanessa has decided to sell some of her clothes to make pocket money, offering a standard price for each type of item. She made a total of $69 by selling 7 dresses and 4 shirts. If she managed to sell each shirt for $5, how much did the dresses sell for each?"""
    # Define the number of dresses and shirts sold
    dresses_sold = 7
    shirts_sold = 4

    # Define the total amount earned by selling dresses and shirts
    total_earned = 69

    # Define the price of each shirt
    shirt_price = 5

    # Calculate the total amount earned by selling all the shirts
    shirts_amount = shirts_sold * shirt_price

    # Calculate the total amount earned by selling all the dresses
    dresses_amount = total_earned - shirts_amount

    # Calculate the price of each dress
    dress_price = dresses_amount / dresses_sold

    # Display the price of each dress
    result = dress_price
    return result

print(solution())