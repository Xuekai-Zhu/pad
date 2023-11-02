def solution():
    """A club opens up and charges $20 to enter.  James buys 2 rounds for his 5 friends.  He also buys 6 drinks for himself. Drinks cost $6 each.  He decides to eat some food so he orders some fried chicken which costs $14.  He leaves a 30% tip on everything he orders.  How much did he spend for the night?"""
    # Define the cost of each item
    ENTRANCE_FEE = 20
    DRINK_PRICE = 6
    FOOD_PRICE = 14

    # Define the number of items James orders
    FRIENDS = 5
    ROUNDS = 2
    DRINKS = 6

    # Calculate the total cost of the drinks
    total_drinks_cost = DRINK_PRICE * DRINKS

    # Calculate the total cost of the rounds for James' friends
    total_rounds_cost = (FRIENDS * ROUNDS) * DRINK_PRICE

    # Calculate the total cost of the food
    total_food_cost = FOOD_PRICE

    # Calculate the subtotal
    subtotal = ENTRANCE_FEE + total_drinks_cost + total_rounds_cost + total_food_cost

    # Calculate the tip
    tip = subtotal * 0.3

    # Calculate the total cost
    total_cost = subtotal + tip

    # Display the total cost
    result = total_cost
    return result

print(solution())