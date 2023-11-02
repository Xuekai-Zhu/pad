def solution():
    
    cheap_gym_fee = 10
    cheap_gym_sign_up_fee = 50
    expensive_gym_fee = 3 * cheap_gym_fee
    expensive_gym_sign_up_fee = expensive_gym_fee * 4
    total_fee = (cheap_gym_fee * 12) + (expensive_gym_fee * 12) + cheap_gym_sign_up_fee + expensive_gym_sign_up_fee
    result = total_fee
    return result

print(solution())