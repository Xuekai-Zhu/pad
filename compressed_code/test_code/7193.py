def solution():
    
    total_gifts = 12
    gifts_wrapped_with_first_two_rolls = 3*1 + 5*1
    gifts_wrapped_with_third_roll = total_gifts - gifts_wrapped_with_first_two_rolls
    result = gifts_wrapped_with_third_roll
    return result

print(solution())