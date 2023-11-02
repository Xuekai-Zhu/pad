def solution():
    total_states = 50
    percentage_owned = 40/total_states
    reward_per_percentage = 2
    total_reward = percentage_owned * total_states * reward_per_percentage
    result = total_reward
    return result

print(solution())