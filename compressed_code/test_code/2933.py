def solution():
    
    procgen_max_reward = 240
    coinrun_max_reward = procgen_max_reward / 2
    ppo_reward = coinrun_max_reward * 0.9
    result = ppo_reward
    return result

print(solution())