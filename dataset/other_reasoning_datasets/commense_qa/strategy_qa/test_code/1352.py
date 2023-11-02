def solution():
    android_based_on = "Linux"
    windows_based_on = "Windows"
    newer_linux_version = "Linux 5.11"
    android_linux_version = "Linux 4.14"
    windows_linux_version = "Linux 3.18"
    # Check which type of smartphone runs the newer version of Linux
    if newer_linux_version in android_linux_version:
        result = "Android smartphones"
    elif newer_linux_version in windows_linux_version:
        result = "Windows smartphones"
    else:
        result = "Neither"
    return result

print(solution())