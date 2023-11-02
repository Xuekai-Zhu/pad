def solution():
    """Faye had $20. Today, her mother gave her twice as much as her money. If she bought ten cupcakes at $1.50 each and five boxes of cookies at $3 per box, how much money did she have left?"""
    # Faye's initial amount of money
    faye_money = 20

    # Faye's mother gave her twice as much as her money
    faye_money += 2 * faye_money

    # Total cost of ten cupcakes at $1.50 each
    cupcake_cost = 10 * 1.5

    # Total cost of five boxes of cookies at $3 per box
    cookie_cost = 5 * 3

    # Total cost of all the items
    total_cost = cupcake_cost + cookie_cost

    # Calculate the money left
    money_left = faye_money - total_cost

    # Display the money left
    result = money_left
    return result

print(solution())