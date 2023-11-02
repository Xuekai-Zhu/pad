def solution():
    """Diana gets 30 minutes of video game time for every hour she reads. Her dad decided to raise her reward by 20%. Diana read for 12 hours this week. How many more minutes of video game time will she get as a result of her raise?"""
    read_time = 12
    original_reward = 30 * read_time
    raise_amount = 0.2 * original_reward
    new_reward = original_reward + raise_amount
    extra_reward = new_reward - original_reward
    result = extra_reward
    return result

print(solution())