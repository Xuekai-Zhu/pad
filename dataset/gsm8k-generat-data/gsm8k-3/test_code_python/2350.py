def solution():
    """For Roger's phone to function optimally, he can have a maximum of 50 apps on his phone. However, the recommended number of apps is 35. If Roger has twice the recommended number of apps, how many apps must he delete for his phone to function optimally again?"""
    # Define the maximum number of apps and the recommended number of apps
    MAX_APPS = 50
    RECOMMENDED_APPS = 35

    # Define the number of apps Roger currently has
    current_apps = 2 * RECOMMENDED_APPS

    # Calculate the number of apps Roger needs to delete
    apps_to_delete = current_apps - MAX_APPS

    # Display the number of apps Roger needs to delete
    result = apps_to_delete
    return result

print(solution())