def solution():
    # Define the cost of one app and the number of apps needed
    app_cost = 4
    num_apps = 15

    # Calculate the total cost of all the apps
    total_cost = app_cost * num_apps

    # Calculate how much money Lidia will have left after buying all the apps
    money_left = 66 - total_cost
    result = money_left
    return result

print(solution())