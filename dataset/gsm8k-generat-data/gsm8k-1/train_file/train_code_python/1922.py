def solution():
    """Katrina saw an ad that said if she signed up for her local recycling program, she could earn $5.00. When she signed up, they told her for every friend that she referred, the friend would receive $5.00 and she would receive another $5.00 per friend. That day, she had 5 friends sign up and another 7 friends by the end of the week. How much money in total did she and her friends make?"""
    initial_reward = 5
    friends_signed_up_first_day = 5
    friends_signed_up_week = 7
    friends_reward = friends_signed_up_first_day + friends_signed_up_week
    total_reward = initial_reward + (friends_reward * 5)
    result = total_reward
    return result

print(solution())