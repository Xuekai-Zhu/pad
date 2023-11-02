def solution():
    """John decides to get gym memberships so he can get in shape. The gym close to his house is close but doesn't have everything he wants so he gets two different gym memberships. The cheap one costs $10 a month and has a sign-up fee of $50. The second gym is 3 times more expensive and it has a sign-up fee of 4 months membership. How much total did he pay in the first year for gym membership?"""
    cheap_gym_fee = 10
    cheap_gym_sign_up_fee = 50
    expensive_gym_fee = 3 * cheap_gym_fee
    expensive_gym_sign_up_fee = expensive_gym_fee * 4
    total_fee = (cheap_gym_fee * 12) + (expensive_gym_fee * 12) + cheap_gym_sign_up_fee + expensive_gym_sign_up_fee
    result = total_fee
    return result

print(solution())