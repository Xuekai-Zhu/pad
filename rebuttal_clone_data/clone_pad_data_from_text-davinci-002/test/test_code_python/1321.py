def solution():
    optimal_apps = 50
    recommended_apps = 35
    num_apps = recommended_apps * 2
    apps_to_delete = num_apps - optimal_apps
    result = apps_to_delete
    return result

print(solution())