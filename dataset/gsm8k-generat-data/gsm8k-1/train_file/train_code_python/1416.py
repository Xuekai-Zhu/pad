def solution():
    """The sum of Mario and Maria's ages now is 7. Mario is 1 year older than Maria. How old is Mario?"""
    total_age = 7
    age_diff = 1
    maria_age = (total_age - age_diff) / 2
    mario_age = maria_age + age_diff
    result = mario_age
    return result

print(solution())