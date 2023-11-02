def solution():
    """Lidia bought a new tablet, and she needs to buy some apps for it. One app costs $4 on average, and Lidia needs 15 of them. She has $66 for this purpose. How much money will she be left with if she buys all the apps she needs?"""
    app_cost = 4
    num_apps = 15
    total_cost = app_cost * num_apps
    remaining_money = 66 - total_cost
    result = remaining_money
    return result

print(solution())