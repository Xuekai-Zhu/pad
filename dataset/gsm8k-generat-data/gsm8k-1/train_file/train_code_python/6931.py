def solution():
    """Diana gets 30 minutes of video game time for every hour she reads. Her dad decided to raise her reward by 20%. Diana read for 12 hours this week. How many more minutes of video game time will she get as a result of her raise?"""
    minutes_per_hour = 30
    reading_hours = 12
    old_reward = minutes_per_hour * reading_hours
    percent_increase = 20
    new_reward = old_reward * (1 + (percent_increase / 100))
    increase = new_reward - old_reward
    result = increase
    return result

print(solution())