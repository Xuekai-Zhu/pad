def solution():
    # Calculate how many apps Roger has
    num_apps = 35 * 2  # twice the recommended number of apps

    # Calculate how many apps he needs to delete to have the maximum of 50 apps
    apps_to_delete = num_apps - 50 

    result = apps_to_delete
    return result

print(solution())