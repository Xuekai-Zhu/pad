def solution():
    
    max_apps = 50
    recommended_apps = 35
    current_apps = 2 * recommended_apps
    delete_apps = current_apps - max_apps
    result = delete_apps
    return result

print(solution())