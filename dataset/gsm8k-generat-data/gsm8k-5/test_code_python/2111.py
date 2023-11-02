def solution():
    download_time = 10  # James spends 10 minutes downloading the game
    install_time = download_time / 2  # James takes half as long to install the game
    tutorial_time = (download_time + install_time) * 3  # James spends three times the combined time on the tutorial

    # Calculate the total time it took James before he can play the main game
    total_time = download_time + install_time + tutorial_time
    result = total_time
    return result

print(solution())