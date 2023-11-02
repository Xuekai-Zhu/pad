def solution():
    """Greg's PPO algorithm obtained 90% of the possible reward on the CoinRun environment. CoinRun's maximum reward is half as much as the maximum ProcGen reward of 240. How much reward did Greg's PPO algorithm get?"""
    procgen_max_reward = 240
    coinrun_max_reward = procgen_max_reward / 2
    algorithm_reward_percent = 90
    algorithm_reward = algorithm_reward_percent / 100 * coinrun_max_reward
    result = algorithm_reward
    return result

print(solution())