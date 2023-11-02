def solution():
    u2_album_length = 42 * 60 + 52  # convert minutes to seconds
    peppa_pig_episode_length = 5 * 60  # convert minutes to seconds
    if u2_album_length < peppa_pig_episode_length:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())