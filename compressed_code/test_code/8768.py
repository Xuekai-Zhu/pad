def solution():
    
    procgen_max_reward = 240
    coinrun_max_reward = procgen_max_reward / 2
    algorithm_reward_percent = 90
    algorithm_reward = algorithm_reward_percent / 100 * coinrun_max_reward
    result = algorithm_reward
    return result

print(solution())