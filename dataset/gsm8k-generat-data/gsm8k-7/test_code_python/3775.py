def solution():
    procgen_max_reward = 240
    coinrun_max_reward = procgen_max_reward / 2
    ppo_percent_reward = 0.9

    # Calculate the actual reward obtained by Greg's PPO algorithm
    ppo_actual_reward = coinrun_max_reward * ppo_percent_reward
    result = ppo_actual_reward
    return result

print(solution())