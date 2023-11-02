def solution():
    samsung_storage = 32 * 1000    # Convert GB to MB
    got_episode_size = 600
    num_got_episodes = 60
    total_got_storage = got_episode_size * num_got_episodes

    if total_got_storage <= samsung_storage:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())