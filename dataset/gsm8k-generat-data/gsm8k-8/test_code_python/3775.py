def solution():
    # Define the maximum reward for CoinRun and ProcGen
    coinrun_max_reward = 240 / 2
    procgen_max_reward = 240

    # Calculate the reward obtained by Greg's PPO algorithm
    reward_obtained = 0.9 * coinrun_max_reward

    result = reward_obtained
    return result

print(solution())