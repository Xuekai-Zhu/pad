def solution():
    recommended_apps = 35  # The recommended number of apps for Roger is 35
    max_apps = 50  # The maximum number of apps for Roger's phone to function optimally is 50
    current_apps = 2 * recommended_apps  # Roger currently has twice the recommended number of apps

    # Calculate the number of apps Roger needs to delete to reach the recommended number
    delete_apps = current_apps - recommended_apps

    # If Roger has more apps than the maximum, he needs to delete the excess
    if current_apps > max_apps:
        delete_apps = current_apps - max_apps

    result = delete_apps
    return result

print(solution())