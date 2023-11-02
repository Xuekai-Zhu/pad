def solution():
    max_apps = 50
    recommended_apps = 35
    current_apps = recommended_apps * 2

    # Calculate the number of apps that Roger needs to delete to have the recommended number of apps
    apps_to_delete = current_apps - recommended_apps
    result = apps_to_delete
    return result

print(solution())