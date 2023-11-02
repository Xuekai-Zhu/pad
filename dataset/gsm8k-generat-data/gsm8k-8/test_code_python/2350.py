def solution():
    # Define the maximum and recommended number of apps
    max_apps = 50
    recommended_apps = 35

    # Calculate Roger's current number of apps
    current_apps = recommended_apps * 2

    # Calculate how many apps he needs to delete
    apps_to_delete = current_apps - max_apps

    result = apps_to_delete
    return result

print(solution())