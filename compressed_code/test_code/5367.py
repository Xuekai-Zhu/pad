def solution():
    
    read_time = 12
    original_reward = 30 * read_time
    raise_amount = 0.2 * original_reward
    new_reward = original_reward + raise_amount
    extra_reward = new_reward - original_reward
    result = extra_reward
    return result

print(solution())