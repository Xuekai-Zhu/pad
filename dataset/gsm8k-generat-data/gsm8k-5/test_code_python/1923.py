def solution():
    initial_reward = 5  # Katrina earned $5 by signing up for the recycling program
    referrals_day1 = 5  # 5 friends signed up on the first day
    referrals_week = 7  # 7 more friends signed up by the end of the week
    referral_reward = 5  # Katrina earned $5 for each friend she referred

    # Calculate the total reward from referrals
    total_referral_reward = referral_reward * (referrals_day1 + referrals_week)

    # Calculate the total amount of money earned by Katrina and her friends
    total_earnings = initial_reward + total_referral_reward
    result = total_earnings
    return result

print(solution())