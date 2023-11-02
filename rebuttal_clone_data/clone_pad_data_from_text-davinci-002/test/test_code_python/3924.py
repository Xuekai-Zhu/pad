def solution():
    safety_limit = 500
    drink_caffeine = 120
    drinks_consumed = 4
    caffeine_consumed = drink_caffeine * drinks_consumed
    remaining_caffeine = safety_limit - caffeine_consumed
    result = remaining_caffeine
    return result

print(solution())