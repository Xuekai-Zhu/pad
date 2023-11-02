def solution():
    initial_signup_bonus = 5
    referral_bonus = 5
    friends_referred = 12
    total_bonus = initial_signup_bonus + friends_referred * referral_bonus
    result = total_bonus
    return result

print(solution())