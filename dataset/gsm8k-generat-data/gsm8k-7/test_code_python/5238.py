def solution():
    cans_recycled = 144
    newspaper_weight = 20  # in kilograms
    can_reward = 0.5
    newspaper_reward = 1.5

    # Calculate the number of 12-can bundles and the corresponding reward
    num_can_bundles = cans_recycled // 12
    can_reward_total = num_can_bundles * can_reward

    # Calculate the number of 5-kg newspaper bundles and the corresponding reward
    num_newspaper_bundles = newspaper_weight // 5
    newspaper_reward_total = num_newspaper_bundles * newspaper_reward

    # Calculate the total reward
    total_reward = can_reward_total + newspaper_reward_total
    result = total_reward
    return result

print(solution())