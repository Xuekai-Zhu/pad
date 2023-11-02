def solution():
    calories_ate = 110 + 310 + 215
    calories_intake_limit = 2500
    calories_still_can_take = calories_intake_limit - calories_ate
    result = calories_still_can_take
    return result

print(solution())