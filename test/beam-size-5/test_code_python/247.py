def solution():
    initial_apps = 61  # Travis had 61 apps on his tablet
    deleted_apps = 9  # Travis deleted 9 apps
    downloaded_apps = 18  # Travis downloaded 18 more apps

    # Calculate the current number of apps on Travis's tablet
    current_apps = initial_apps - deleted_apps + downloaded_apps
    result = current_apps
    return result

print(solution())