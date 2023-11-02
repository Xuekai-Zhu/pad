def solution():
    """Katrina saw an ad that said if she signed up for her local recycling program, she could earn $5.00.  When she signed up, they told her for every friend that she referred, the friend would receive $5.00 and she would receive another $5.00 per friend.  That day, she had 5 friends sign up and another 7 friends by the end of the week.  How much money in total did she and her friends make?"""
    # Define the amount earned per referral
    REFERRAL_EARNINGS = 5

    # Sign-up earnings
    sign_up_earnings = 5

    # Referral earnings from 5 friends
    friend_referral_earnings_1 = 5 * 5  # 5 friends signed up
    friend_referral_earnings_2 = 7 * 5  # 7 friends signed up by end of week

    # Total earnings
    total_earnings = sign_up_earnings + friend_referral_earnings_1 + friend_referral_earnings_2

    # Display the total earnings
    result = total_earnings
    return result

print(solution())