def solution():
    # Calculate CoinRun's maximum reward
    max_coinrun_reward = 240/2  # CoinRun's maximum reward is half as much as the maximum ProcGen reward of 240

    # Calculate the reward obtained by Greg's PPO algorithm
    ppo_reward = max_coinrun_reward * 0.9  # Greg's PPO algorithm obtained 90% of the possible reward on the CoinRun environment

    result = ppo_reward
    return result

print(solution())