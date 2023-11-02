def solution():
    """James spends 10 minutes downloading a game, half as long installing it, and triple that combined amount of time going through the tutorial. How long does it take before he can play the main game?"""
    # Define the time it takes to download the game
    download_time = 10

    # Define the time it takes to install the game
    install_time = download_time / 2

    # Define the combined time for download and install
    download_install_time = download_time + install_time

    # Define the time it takes to go through the tutorial
    tutorial_time = download_install_time * 3

    # Define the total time before playing the main game
    total_time = download_time + install_time + tutorial_time

    result = total_time
    return result

print(solution())