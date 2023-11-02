def solution():
    """Five friends eat at Wendy's and ordered the following: a platter of Taco Salad that cost $10, 5 orders of Dave's Single hamburger that cost $5 each, 4 sets of french fries that cost $2.50, and 5 cups of peach lemonade that cost $2 each. How much will each of them pay if they will split the bill equally?"""
    # Define the prices of each item
    TACO_SALAD_PRICE = 10
    HAMBURGER_PRICE = 5
    FRIES_PRICE = 2.5
    LEMONADE_PRICE = 2

    # Define the quantity of each item
    taco_salad_qty = 1
    hamburger_qty = 5
    fries_qty = 4
    lemonade_qty = 5

    # Calculate the total cost of each item
    taco_salad_cost = TACO_SALAD_PRICE * taco_salad_qty
    hamburger_cost = HAMBURGER_PRICE * hamburger_qty
    fries_cost = FRIES_PRICE * fries_qty
    lemonade_cost = LEMONADE_PRICE * lemonade_qty

    # Calculate the total cost of the bill
    total_cost = taco_salad_cost + hamburger_cost + fries_cost + lemonade_cost

    # Divide the total cost by the number of friends
    num_friends = 5
    cost_per_friend = total_cost / num_friends

    # Display the cost per friend
    result = cost_per_friend
    return result

print(solution())