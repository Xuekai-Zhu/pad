def solution():
    """Jane is shopping for some fruit.  She sees a stand of fruit advertising 10 apples for $2, and another one advertising 5 oranges for $1.50.  Assuming there's no price discount for buying in bulk, how much would Jane spend in cents if she bought 12 of the cheaper of the two fruits?"""
    # Calculate the cost of 12 apples
    apple_price = 2 / 10 # cost per apple
    apple_cost = apple_price * 12

    # Calculate the cost of 12 oranges
    orange_price = 1.5 / 5 # cost per orange
    orange_cost = orange_price * 12

    # Determine which fruit is cheaper
    if apple_price < orange_price:
        cheaper_fruit_cost = apple_cost
    else:
        cheaper_fruit_cost = orange_cost

    # Convert to cents and display the cost of 12 of the cheaper fruit
    result = int(cheaper_fruit_cost * 100)
    return result

print(solution())