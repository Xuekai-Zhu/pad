def solution():
    download_time = 10
    install_time = download_time / 2
    tutorial_time = (download_time + install_time) * 3
    total_time = download_time + install_time + tutorial_time
    result = total_time
    return result

print(solution())