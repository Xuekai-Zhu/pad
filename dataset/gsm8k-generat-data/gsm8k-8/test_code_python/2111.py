def solution():
    # Define the time spent downloading and installing the game
    download_time = 10  # in minutes
    install_time = download_time / 2  # in minutes

    # Calculate the total time spent on downloading and installing
    total_time = download_time + install_time  # in minutes

    # Calculate the time spent on the tutorial
    tutorial_time = 3 * total_time  # in minutes

    # Calculate the total time spent before playing the main game
    total_time_before_playing = total_time + tutorial_time  # in minutes

    result = total_time_before_playing
    return result

print(solution())