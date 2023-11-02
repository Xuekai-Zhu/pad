def solution():
    """Vanessa has decided to sell some of her clothes to make pocket money, offering a standard price for each type of item. She made a total of $69 by selling 7 dresses and 4 shirts. If she managed to sell each shirt for $5, how much did the dresses sell for each?"""
    # Define the number of dresses and shirts sold
    dresses_sold = 7
    shirts_sold = 4

    # Define the total amount earned from selling the clothes
    total_earned = 69

    # Define the cost of each shirt
    shirt_cost = 5

    # Calculate the total earned from selling the shirts
    shirt_earned = shirts_sold * shirt_cost

    # Calculate the total earned from selling the dresses
    dress_earned = total_earned - shirt_earned

    # Calculate the cost of each dress
    dress_cost = dress_earned / dresses_sold

    # Return the result
    result = round(dress_cost, 2)
    return result

print(solution())