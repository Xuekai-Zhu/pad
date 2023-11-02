def solution():
    """Greg's PPO algorithm obtained 90% of the possible reward on the CoinRun environment. CoinRun's maximum reward is half as much as the maximum ProcGen reward of 240. How much reward did Greg's PPO algorithm get?"""
    # Define the maximum reward for ProcGen
    max_procgen_reward = 240

    # Calculate the maximum reward for CoinRun
    max_coinrun_reward = max_procgen_reward / 2

    # Calculate the reward obtained by Greg's algorithm on CoinRun
    gregs_reward = max_coinrun_reward * 0.9

    # Return the result
    result = gregs_reward
    return result

print(solution())