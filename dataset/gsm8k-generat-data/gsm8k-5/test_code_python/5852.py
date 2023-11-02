def solution():
    app_cost = 4  # The cost of one app is $4 on average
    num_apps = 15  # Lidia needs to buy 15 apps
    budget = 66  # Her budget for apps is $66

    # Calculate the total cost of buying all the apps
    total_cost = app_cost * num_apps

    # Calculate the amount Lidia will have left after buying all the apps
    remaining_budget = budget - total_cost
    result = remaining_budget
    return result

print(solution())