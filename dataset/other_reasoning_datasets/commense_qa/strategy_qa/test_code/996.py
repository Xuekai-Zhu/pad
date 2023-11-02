def solution():
    apps_require_internet = True
    offline_apps_available = True
    internet_connection_needed_to_download = True
    if apps_require_internet and not offline_apps_available and internet_connection_needed_to_download:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())