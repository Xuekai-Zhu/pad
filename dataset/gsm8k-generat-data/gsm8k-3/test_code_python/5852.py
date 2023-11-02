def solution():
    """Lidia bought a new tablet, and she needs to buy some apps for it. One app costs $4 on average, and Lidia needs 15 of them. She has $66 for this purpose. How much money will she be left with if she buys all the apps she needs?"""
    # Define the cost of each app
    APP_COST = 4

    # Define the number of apps Lidia needs to buy
    num_apps = 15

    # Define Lidia's budget for buying apps
    budget = 66

    # Calculate the total cost of all the apps Lidia needs to buy
    total_cost = num_apps * APP_COST

    # Calculate the amount of money Lidia will be left with after buying all the apps she needs
    leftover_money = budget - total_cost

    # Display the amount of money Lidia will be left with
    result = leftover_money
    return result

print(solution())