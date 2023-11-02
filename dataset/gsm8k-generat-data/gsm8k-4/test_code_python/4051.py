def solution():
    """Five friends eat at Wendy's and ordered the following: a platter of Taco Salad that cost $10, 5 orders of Dave's Single hamburger that cost $5 each, 4 sets of french fries that cost $2.50, and 5 cups of peach lemonade that cost $2 each. How much will each of them pay if they will split the bill equally?"""
    # Define the prices of the food and drinks
    taco_salad = 10
    hamburger = 5
    fries = 2.5
    lemonade = 2

    # Calculate the total bill
    total_bill = (taco_salad + (5 * hamburger) + (4 * fries) + (5 * lemonade))

    # Calculate the amount each friend needs to pay
    amount_per_friend = total_bill / 5

    result = amount_per_friend
    return result

print(solution())