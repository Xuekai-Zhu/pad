def solution():
    """Greg's PPO algorithm obtained 90% of the possible reward on the CoinRun environment. CoinRun's maximum reward is half as much as the maximum ProcGen reward of 240. How much reward did Greg's PPO algorithm get?"""
    # Define the maximum reward for CoinRun and ProcGen
    COINRUN_MAX_REWARD = 240 / 2

    # Calculate the reward that Greg's PPO algorithm obtained
    ppo_reward = 0.9 * COINRUN_MAX_REWARD

    # Display the reward obtained by Greg's PPO algorithm
    result = ppo_reward
    return result

print(solution())