def solution():
    # Define the relationship between Super Mario, video games, electronic devices, and electricity
    super_mario_is_video_game = True
    video_games_are_electronic_devices = True
    electronic_devices_require_electricity = True
    # Check if Super Mario requires electricity to play
    if super_mario_is_video_game and video_games_are_electronic_devices and electronic_devices_require_electricity:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())