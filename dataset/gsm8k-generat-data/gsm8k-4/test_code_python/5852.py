def solution():
    """Lidia bought a new tablet, and she needs to buy some apps for it. One app costs $4 on average, and Lidia needs 15 of them. She has $66 for this purpose. How much money will she be left with if she buys all the apps she needs?"""
    # Define the price and quantity of apps
    app_price = 4
    app_quantity = 15

    # Calculate the total cost of the apps
    total_cost = app_price * app_quantity

    # Calculate the amount of money Lidia will be left with
    left_money = 66 - total_cost

    # return the result
    result = left_money
    return result

print(solution())