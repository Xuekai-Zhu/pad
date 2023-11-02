def solution():
    
    max_apps = 50
    recommended_apps = 35
    current_apps = 2 * recommended_apps
    apps_to_delete = current_apps - max_apps
    result = apps_to_delete
    return result

print(solution())