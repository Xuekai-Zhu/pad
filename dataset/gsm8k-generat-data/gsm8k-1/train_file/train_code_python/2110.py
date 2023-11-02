def solution():
    """James spends 10 minutes downloading a game, half as long installing it, and triple that combined amount of time going through the tutorial. How long does it take before he can play the main game?"""
    download_time = 10
    install_time = download_time / 2
    tutorial_time = (download_time + install_time) * 3
    total_time = download_time + install_time + tutorial_time
    result = total_time
    return result

print(solution())