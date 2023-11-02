def solution():
    initial_reward = 5.0
    referral_reward = 5.0

    num_friends_day1 = 5
    num_friends_week1 = 7

    # Calculate Katrina's reward for signing up
    katrina_reward = initial_reward

    # Calculate the total reward for the friends who signed up on the first day
    day1_reward = num_friends_day1 * referral_reward

    # Calculate the total reward for the friends who signed up by the end of the week
    week1_reward = num_friends_week1 * referral_reward

    # Calculate the total earnings for Katrina and her friends
    total_earnings = katrina_reward + day1_reward + week1_reward
    result = total_earnings
    return result

print(solution())