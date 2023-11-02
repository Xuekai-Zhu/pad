def solution():
    """Travis had 61 apps on his tablet. He deleted 9 apps he didn't use anymore and downloaded 18 more. How many apps are on his tablet now?"""
    initial_apps = 61
    deleted_apps = 9
    downloaded_apps = 18
    total_apps = initial_apps - deleted_apps + downloaded_apps
    result = total_apps
    return result

print(solution())