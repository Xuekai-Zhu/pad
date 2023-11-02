def solution():
    download_time = 10  # minutes
    install_time = download_time / 2  # half the download time
    tutorial_time = 3 * (download_time + install_time)  # triple the combined download and install time
    total_time = download_time + install_time + tutorial_time
    result = total_time
    return result

print(solution())