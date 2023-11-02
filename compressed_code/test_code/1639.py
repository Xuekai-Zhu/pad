def solution():
    
    download_time = 10
    install_time = download_time / 2
    tutorial_time = 3 * (download_time + install_time)
    total_time = download_time + install_time + tutorial_time
    result = total_time
    return result

print(solution())