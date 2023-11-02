def solution():
    
    cheap_gym_monthly = 10
    cheap_gym_sign_up = 50
    expensive_gym_monthly = cheap_gym_monthly * 3
    expensive_gym_sign_up = expensive_gym_monthly * 4
    total_cost = cheap_gym_monthly * 12 + cheap_gym_sign_up + expensive_gym_monthly * 12 + expensive_gym_sign_up
    result = total_cost
    return result

print(solution())