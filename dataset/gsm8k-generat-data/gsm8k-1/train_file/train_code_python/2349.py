def solution():
    """For Roger's phone to function optimally, he can have a maximum of 50 apps on his phone. However, the recommended number of apps is 35. If Roger has twice the recommended number of apps, how many apps must he delete for his phone to function optimally again?"""
    max_apps = 50
    recommended_apps = 35
    current_apps = 2 * recommended_apps
    apps_to_delete = current_apps - max_apps
    result = apps_to_delete
    return result

print(solution())