def solution():
    max_procgen_reward = 240
    max_coinrun_reward = max_procgen_reward / 2  # CoinRun's maximum reward is half of ProcGen's maximum reward
    ppo_reward_percentage = 90
    ppo_reward = ppo_reward_percentage / 100 * max_coinrun_reward  # Calculate the PPO reward

    result = ppo_reward
    return result

print(solution())