def solution():
    """Faye had $20. Today, her mother gave her twice as much as her money. If she bought ten cupcakes at $1.50 each and five boxes of cookies at $3 per box, how much money did she have left?"""
    # Define the initial amount of money Faye had
    initial_money = 20

    # Calculate the amount of money Faye's mother gave her
    mother_money = initial_money * 2

    # Calculate the total amount of money Faye has
    total_money = initial_money + mother_money

    # Calculate the cost of the cupcakes
    cupcakes_cost = 1.5 * 10

    # Calculate the cost of the boxes of cookies
    cookies_cost = 3 * 5

    # Calculate the total cost of the items purchased
    total_cost = cupcakes_cost + cookies_cost

    # Calculate the amount of money Faye has left
    money_left = total_money - total_cost

    # Return the result
    result = money_left
    return result

print(solution())